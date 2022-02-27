log "Programing FPGA"

$CDF = $args[0]

### To generate this just create a cdf programming file using the programmer in quartus, ensure it works, and then save it

quartus_pgm $CDF

