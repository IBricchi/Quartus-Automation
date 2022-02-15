$PREVD = $pwd

$CACHE_RANGE = (2048, 65536, 4096, 8192, 16384, 32768, 131072, 1024)

./scripts/example/change-cache.ps1 128 128

# foreach ($dcache in $CACHE_RANGE){
#     foreach($icache in $CACHE_RANGE){
#     }
# }

Set-Location $PREVD