$PREVD = $pwd
cd <parent of scripts folder>

# load config data
. ./scripts/config.ps1

$dcache = $args[0]
$icache = $args[1]

# define range of values for c file generation
$STEP_RANGE = ("5","1/8.0","1/1024.0")
$N_RANGE = ("52","2051","261121")

# VERY IMPORTANT MUST BE SET AND BE UNIQUE PER QUARTUS CONFIGURATION
# Used for caching past quartus configurations so that if the same config is used
# in multiple test cases it doesn't need to be re-compiled which can significantly speed things up
# Important to note unique to quartus configuration, this does not include any of the eclipse stuff,
# only quartus files such as QSYS files
$BUILD_NAME="task3-dcache-$dcache-icache-$icache"

# Generate qsys tcl file for specific dcache and icache
python "$pwd/scripts/example/generate/gen_qsys_task2_cache.py" $dcache $icache $QP

# loop over c test cases
foreach ($i in (3))
{
    # Specify name of output directoy to store all run information
    # Includes compilation reports, summary, and output of nios2-terminal
    $NAME="$BUILD_NAME-test-$i"

    # Generate c file for specific test
    $STEP = $STEP_RANGE[$i-1]
    $N = $N_RANGE[$i-1]
    python "$pwd/scripts/example/generate/gen_c_file.py" $STEP $N $i $dcache $icache $EP
    
    # Log test case to terminal
    Write-Output "-------------------------------------------------------------------------------"
    log ("Running test " + $NAME)
    Write-Output "-------------------------------------------------------------------------------"
    
    # Run build command (also runs, and saves everything, more lika a run-all command)
    ./scripts/build-all.ps1

    # Pring outtput of nios-termianl to screen
    Get-Content "$SP/out/$NAME/nios.out"
}

Set-Location $PREVD