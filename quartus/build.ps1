$PREVD = $pwd
cd $QP
log "Generating QSYS file"
qsys-script --script=./first_nios2_system.tcl 2> $null
log "Building QSYS file"
qsys-generate ./first_nios2_system.qsys -syn=VERILOG -bsf -od="$QSYS_PATH" 2> $null
log "Compiling Quartus project"
quartus_sh --flow compile $QP_NAME > $null
cd $PREVD