$SOURCE = $QP
$TARGET = $args[-1]

$FILES = @(
    "hello_world.asm.rpt"
    "hello_world.done"
    "hello_world.fit.rpt"
    "hello_world.fit.summary"
    "hello_world.flow.rpt"
    "hello_world.map.rpt"
    "hello_world.map.summary"
    "hello_world.sta.rpt"
    "hello_world.sta.summary"
    "first_nios2_system.tcl"
)

if (Test-Path -Path $TARGET)
{
    log "Found previous data folder in specified save location"
    log "Creating backup archive of current data"
    log "Only one backup is maintained at any time"
    $compress = @{
        Path = $TARGET
        CompressionLevel = "Fastest"
        DestinationPath = "$SP/out/backup.zip"
    }
    Compress-Archive @compress
    rm $TARGET -r -fo
}

log "Saving reports from quartus compilation"
mkdir $TARGET > $null
foreach ( $FILE in $FILES )
{
    cp "$SOURCE/$FILE" $TARGET
}

if (Test-Path "$SP/out/backup.zip")
{
    mv "$SP/out/backup.zip" $TARGET
}