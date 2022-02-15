$PREVD = $pwd
cd $QP
log "Generating QSYS file"
qsys-script --script=./first_nios2_system.tcl 2> $null
log "Building QSYS file"
qsys-generate ./first_nios2_system.qsys -syn=VERILOG -bsf -od="$QP/first_nios2_system" 2> $null
log "Compiling Quartus project"
quartus_sh --flow compile hello_world > $null
cd $PREVD