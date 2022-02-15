$PREVD = $pwd

Set-Location "$EP/software/$EP_NAME" 
log "Running Project"
& 'Nios II Command Shell.bat' nios2-download -g "./${EP_NAME}.elf" > $null

# [console]::beep(500,1000)

Set-Location $PREVD
