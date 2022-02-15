$SP = absolute path to scripts folder

$CACHE_RANGE = (1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072)

Write-Output "dcache size,icache size,test case, steps in testcase, stepsize in test case, result, ticks taken, Logic utilization (in ALMs), Logic utilization (in ALMs) usage, Total registers, Total block memory bits, Total block memory bits usage, Total RAM Blocks, Total RAM Blocks usage, Slack conditions met"

foreach ($dcache in $CACHE_RANGE) {
    foreach ($icache in $CACHE_RANGE) {
        foreach ($i in (1, 2, 3)) {
            $NAME = "task3-dcache-$dcache-icache-$icache-test-$i"

            # GET OUTPUT FROM NIOS
            $NIOS_OUT = Get-Content -Path "$SP/out/$NAME/nios.out" | Select-Object -First 2 | Select-Object -Last 1
            $NIOS_OUT -match "AVG: DCACHE: .* ICACHE: .* TEST: $i STEPS: (?<steps>.*) STEP_SIZE: (?<step_size>.*) Result: (?<res>.*) took (?<ticks>.*) ticks" > $null

            $STEPS = $matches['steps']
            $STEP_SIZE = $matches['step_size']
            $RES = $matches['res']
            $TICKS = $matches['ticks']

            # GET DATA FROM FIT STAGE
            $FIT_SUMMARY = Get-Content -Path "$SP/out/$NAME/hello_world.fit.summary" -Raw
            $FIT_SUMMARY -match
".*
Logic utilization \(in ALMs\) : (?<logic_util>.*) / (?<logic_util_max>.*) \(.*
Total registers : (?<total_registers>.*).*
Total pins : (?<total_pins>.*) / (?<total_pins_max>.*) \(.*
Total virtual pins : (?<total_virtual_pins>.*).*
Total block memory bits : (?<total_block_memory_bits>.*) / (?<total_block_memory_bits_max>.*) \(.*
Total RAM Blocks : (?<total_ram_blocks>.*) / (?<total_ram_blocks_max>.*) \(.*
Total DSP Blocks : (?<total_dsp_blocks>.*) / (?<total_dsp_blocks_max>.*) \(.*
Total HSSI RX PCSs : (?<toal_hssi_rx_pcss>.*).*
Total HSSI PMA RX Deserializers : (?<total_hssi_pma_rx_deserializers>.*).*
Total HSSI TX PCSs : (?<total_hssi_tx_pcss>.*).*
Total HSSI PMA TX Serializers : (?<total_hssi_pma_tx_serializers>.*).*
Total PLLs : (?<total_plls>.*) / (?<total_plls_max>.*) \(.*
Total DLLs : (?<total_dlls>.*) / (?<total_dlls_max>.*) \(.*" > $null
            $LOGIC_UTIL = [double]$matches['logic_util']
            $LOGIC_UTIL_USAGE = $LOGIC_UTIL / [double]$matches['logic_util_max']
            $TOTAL_REGISTERS = [double]$matches['total_registers']
            $TOTAL_BLOCK_MEMORY_BITS = [double]$matches['total_block_memory_bits']
            $TOTAL_BLOCK_MEMORY_BITS_USAGE = $TOTAL_BLOCK_MEMORY_BITS / [double]$matches['total_block_memory_bits_max']
            $TOTAL_RAM_BLOCKS = [double]$matches['total_ram_blocks']
            $TOTAL_RAM_BLOCKS_USAGE = $TOTAL_RAM_BLOCKS / [double]$matches['total_ram_blocks_max']

            # GET DATA FROM TIMING STAGE
            $ALL_SLACK_POSITIVE = $true
            foreach ($LINE in Get-Content -Path "$SP/out/$NAME/hello_world.sta.summary"){
                if ($LINE -match "Slack : (?<slack>.*)"){
                    if ([double]$matches['slack'] -lt 0.0){
                        $ALL_SLACK_POSITIVE = $false
                    }
                }
            }
            $SLACK_CONDITIONS_MET = ""
            if ($ALL_SLACK_POSITIVE){
                $SLACK_CONDITIONS_MET = "MET"
            }
            else{
                $SLACK_CONDITIONS_MET = "NOT MET"
            }

            Write-Output "$dcache,$icache,$i,$STEPS,$STEP_SIZE,$RES,$TICKS,$LOGIC_UTIL,$LOGIC_UTIL_USAGE,$TOTAL_REGISTERS,$TOTAL_BLOCK_MEMORY_BITS,$TOTAL_BLOCK_MEMORY_BITS_USAGE,$TOTAL_RAM_BLOCKS,$TOTAL_RAM_BLOCKS_USAGE,$SLACK_CONDITIONS_MET"
        }
    }
}
