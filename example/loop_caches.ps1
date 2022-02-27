$PREVD = $pwd

Set-Location "C:/Users/ibricchi/Documents/Quartus-Automation"
# load config data
. ./config.ps1

$CACHE_RANGE = (2048, 65536, 4096, 8192, 16384, 32768, 131072, 1024)

foreach ($dcache in $CACHE_RANGE){
    foreach($icache in $CACHE_RANGE){
        ./example/change-cache.ps1 $dcache $icache
    }
}

Set-Location $PREVD