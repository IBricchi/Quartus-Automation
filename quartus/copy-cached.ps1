$SOURCE = $args[-1]
$TARGET = $QP

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
    "hello_world_time_limited.sof"
    "first_nios2_system.sopcinfo"
)

# $FILES = @(
#     "hello_world.asm.rpt"
#     "hello_world.done"
#     "hello_world.fit.rpt"
#     "hello_world.fit.summary"
#     "hello_world.flow.rpt"
#     "hello_world.map.rpt"
#     "hello_world.map.summary"
#     "hello_world.sta.rpt"
#     "hello_world.sta.summary"
#     "first_nios2_system.tcl"
#     "hello_world_time_limited.sof"
#     "first_nios2_system.sopcinfo"
#     "first_nios2_system"
#     "db"
#     "c5_pin_model_dump.txt"
#     "first_nios2_system.qsys"
#     "hello_world.jdi"
#     "hello_world.pin"
#     "hello_world.qsf"
#     "hello_world.sld"
# )

log "Copying cached quartus build info"
foreach ( $FILE in $FILES )
{
    cp "$SOURCE/$FILE" $TARGET -fo
}