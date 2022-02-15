$PREVD = $pwd
cd <parent of scripts folder>

. ./scripts/config.ps1

$dcache = $args[0]
$icache = $args[1]

$STEP_RANGE = ("5","1/8.0","1/1024.0")
$N_RANGE = ("52","2051","261121")

$BUILD_NAME="task2-dcache-$dcache-icache-$icache"
python "$pwd/scripts/example/generate/gen_qsys_task2_cache.py" $dcache $icache $QP

foreach ($i in (1,2))
{
    $NAME="$BUILD_NAME-test-$i"
    $STEP = $STEP_RANGE[$i-1]
    $N = $N_RANGE[$i-1]
    python "$pwd/scripts/example/generate/gen_c_file.py" $STEP $N $i $dcache $icache $EP
    Write-Output "-------------------------------------------------------------------------------"
    log ("Running test " + $NAME)
    Write-Output "-------------------------------------------------------------------------------"
    ./scripts/build-all.ps1
    Get-Content "$SP/out/$NAME/nios.out"
}

Set-Location $PREVD