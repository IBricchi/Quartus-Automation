$PREVD = $pwd

$BUILD_FOLDER = "$SP/build/$BUILD_NAME"
$OUT_FOLDER = "$SP/out/$NAME/"

$BUILD_CACHED = Test-Path -Path $BUILD_FOLDER

# Build Quartus Project
if ($BUILD_CACHED) {
    log "Using cached quartus build files"
    ./quartus/copy-cached.ps1 $BUILD_FOLDER
}
else {
    ./quartus/build.ps1
}

# Create Quartus Programming Process
$programmer_process = New-Object System.Diagnostics.ProcessStartInfo
$programmer_process.FileName = "powershell.exe" #process file
$programmer_process.Arguments = "-File $SP/quartus/program.ps1 $CDF" #process arguments
$programmer_process.UseShellExecute = $false #start the process from it's own executable file
$programmer_process.RedirectStandardInput = $true #enable the process to read from standard input
$programmer_process.RedirectStandardOutput = $true

log "Programing FPGA"
$programmer = [System.Diagnostics.Process]::Start($programmer_process)

# Create Quartus Programming Process
$terminal_process = New-Object System.Diagnostics.ProcessStartInfo
$terminal_process.FileName = "nios2-terminal" #process file
$terminal_process.UseShellExecute = $false #start the process from it's own executable file
$terminal_process.RedirectStandardInput = $true #enable the process to read from standard input
$terminal_process.RedirectStandardOutput = $true

./eclipse/build.ps1

log "Starting Nios Terminal"
$terminal = [System.Diagnostics.Process]::Start($terminal_process)
$terminal.StandardOutput.DiscardBufferedData()

./eclipse/program.ps1

### To extract data from nios 2, guards need to be printed both before and after the data wanting to be extracted is found
### I recomend having a print like statement at the begining of main with ---START <something unique for test case> ---
### And ending the main function with ---STOP---
### The reason something unique must be used is that due to the way we're looping over so many configurations I found that sometimes
### data from a previous loop is displayed again, to avoid this data from being read, the unique data provides an extra check
### in the example test case you'll se that the guard is being generated to be unique for the different caches and test cases
### I dinamically create the c file for each test case so I just alter what the printf statement is displaying at that stage

# Find ---START---
$LINE = $terminal.StandardOutput.ReadLine()
while ($LINE -ne "---START $GAURD---" ) {
    $LINE = $terminal.StandardOutput.ReadLine()
}

# Read lines till stop
$SAVED_LINES = @()
$LINE = $terminal.StandardOutput.ReadLine()
while ($LINE -ne "---STOP---" ) {
    $SAVED_LINES += $LINE
    $LINE = $terminal.StandardOutput.ReadLine()
}

$terminal.StandardOutput.DiscardBufferedData()
$terminal.Kill()

./quartus/save.ps1 $OUT_FOLDER
New-Item -Path ($OUT_FOLDER + "nios.out") -ItemType File > $null
foreach ($LINE in $SAVED_LINES) {
    Add-Content -Value $LINE -PATH ($OUT_FOLDER + "nios.out")
}

if (!$BUILD_CACHED) {
    log "Caching quartus build files."
    ./quartus/cache.ps1 $BUILD_FOLDER
}

$programmer.StandardInput.WriteLine("q")

Set-Location $PREVD