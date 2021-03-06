import sys

dcache_size = sys.argv[1]
icache_size = sys.argv[2]
qp = sys.argv[3]

first_nios2_system = (f"""# qsys scripting (.tcl) file for first_nios2_system
package require -exact qsys 16.0

create_system {{first_nios2_system}}

set_project_property DEVICE_FAMILY {{Cyclone V}}
set_project_property DEVICE {{5CSEMA5F31C6}}
set_project_property HIDE_FROM_IP_CATALOG {{false}}

# Instances and instance parameters
# (disabled instances are intentionally culled)
add_instance clk_0 clock_source 18.1
set_instance_parameter_value clk_0 {{clockFrequency}} {{50000000.0}}
set_instance_parameter_value clk_0 {{clockFrequencyKnown}} {{1}}
set_instance_parameter_value clk_0 {{resetSynchronousEdges}} {{NONE}}

add_instance cpu altera_nios2_gen2 18.1
set_instance_parameter_value cpu {{bht_ramBlockType}} {{Automatic}}
set_instance_parameter_value cpu {{breakOffset}} {{32}}
set_instance_parameter_value cpu {{breakSlave}} {{None}}
set_instance_parameter_value cpu {{cdx_enabled}} {{0}}
set_instance_parameter_value cpu {{cpuArchRev}} {{1}}
set_instance_parameter_value cpu {{cpuID}} {{0}}
set_instance_parameter_value cpu {{cpuReset}} {{0}}
set_instance_parameter_value cpu {{data_master_high_performance_paddr_base}} {{0}}
set_instance_parameter_value cpu {{data_master_high_performance_paddr_size}} {{0.0}}
set_instance_parameter_value cpu {{data_master_paddr_base}} {{0}}
set_instance_parameter_value cpu {{data_master_paddr_size}} {{0.0}}
set_instance_parameter_value cpu {{dcache_bursts}} {{false}}
set_instance_parameter_value cpu {{dcache_numTCDM}} {{0}}
set_instance_parameter_value cpu {{dcache_ramBlockType}} {{Automatic}}
set_instance_parameter_value cpu {{dcache_size}} {{{dcache_size}}}
set_instance_parameter_value cpu {{dcache_tagramBlockType}} {{Automatic}}
set_instance_parameter_value cpu {{dcache_victim_buf_impl}} {{ram}}
set_instance_parameter_value cpu {{debug_OCIOnchipTrace}} {{_128}}
set_instance_parameter_value cpu {{debug_assignJtagInstanceID}} {{0}}
set_instance_parameter_value cpu {{debug_datatrigger}} {{0}}
set_instance_parameter_value cpu {{debug_debugReqSignals}} {{0}}
set_instance_parameter_value cpu {{debug_enabled}} {{1}}
set_instance_parameter_value cpu {{debug_hwbreakpoint}} {{0}}
set_instance_parameter_value cpu {{debug_jtagInstanceID}} {{0}}
set_instance_parameter_value cpu {{debug_traceStorage}} {{onchip_trace}}
set_instance_parameter_value cpu {{debug_traceType}} {{none}}
set_instance_parameter_value cpu {{debug_triggerArming}} {{1}}
set_instance_parameter_value cpu {{dividerType}} {{no_div}}
set_instance_parameter_value cpu {{exceptionOffset}} {{32}}
set_instance_parameter_value cpu {{exceptionSlave}} {{sdram.s1}}
set_instance_parameter_value cpu {{fa_cache_line}} {{2}}
set_instance_parameter_value cpu {{fa_cache_linesize}} {{0}}
set_instance_parameter_value cpu {{flash_instruction_master_paddr_base}} {{0}}
set_instance_parameter_value cpu {{flash_instruction_master_paddr_size}} {{0.0}}
set_instance_parameter_value cpu {{icache_burstType}} {{None}}
set_instance_parameter_value cpu {{icache_numTCIM}} {{0}}
set_instance_parameter_value cpu {{icache_ramBlockType}} {{Automatic}}
set_instance_parameter_value cpu {{icache_size}} {{{icache_size}}}
set_instance_parameter_value cpu {{icache_tagramBlockType}} {{Automatic}}
set_instance_parameter_value cpu {{impl}} {{Fast}}
set_instance_parameter_value cpu {{instruction_master_high_performance_paddr_base}} {{0}}
set_instance_parameter_value cpu {{instruction_master_high_performance_paddr_size}} {{0.0}}
set_instance_parameter_value cpu {{instruction_master_paddr_base}} {{0}}
set_instance_parameter_value cpu {{instruction_master_paddr_size}} {{0.0}}
set_instance_parameter_value cpu {{io_regionbase}} {{0}}
set_instance_parameter_value cpu {{io_regionsize}} {{0}}
set_instance_parameter_value cpu {{master_addr_map}} {{0}}
set_instance_parameter_value cpu {{mmu_TLBMissExcOffset}} {{0}}
set_instance_parameter_value cpu {{mmu_TLBMissExcSlave}} {{None}}
set_instance_parameter_value cpu {{mmu_autoAssignTlbPtrSz}} {{1}}
set_instance_parameter_value cpu {{mmu_enabled}} {{0}}
set_instance_parameter_value cpu {{mmu_processIDNumBits}} {{8}}
set_instance_parameter_value cpu {{mmu_ramBlockType}} {{Automatic}}
set_instance_parameter_value cpu {{mmu_tlbNumWays}} {{16}}
set_instance_parameter_value cpu {{mmu_tlbPtrSz}} {{7}}
set_instance_parameter_value cpu {{mmu_udtlbNumEntries}} {{6}}
set_instance_parameter_value cpu {{mmu_uitlbNumEntries}} {{4}}
set_instance_parameter_value cpu {{mpu_enabled}} {{0}}
set_instance_parameter_value cpu {{mpu_minDataRegionSize}} {{12}}
set_instance_parameter_value cpu {{mpu_minInstRegionSize}} {{12}}
set_instance_parameter_value cpu {{mpu_numOfDataRegion}} {{8}}
set_instance_parameter_value cpu {{mpu_numOfInstRegion}} {{8}}
set_instance_parameter_value cpu {{mpu_useLimit}} {{0}}
set_instance_parameter_value cpu {{mpx_enabled}} {{0}}
set_instance_parameter_value cpu {{mul_32_impl}} {{0}}
set_instance_parameter_value cpu {{mul_64_impl}} {{0}}
set_instance_parameter_value cpu {{mul_shift_choice}} {{1}}
set_instance_parameter_value cpu {{ocimem_ramBlockType}} {{Automatic}}
set_instance_parameter_value cpu {{ocimem_ramInit}} {{0}}
set_instance_parameter_value cpu {{regfile_ramBlockType}} {{Automatic}}
set_instance_parameter_value cpu {{register_file_por}} {{0}}
set_instance_parameter_value cpu {{resetOffset}} {{0}}
set_instance_parameter_value cpu {{resetSlave}} {{sdram.s1}}
set_instance_parameter_value cpu {{resetrequest_enabled}} {{1}}
set_instance_parameter_value cpu {{setting_HBreakTest}} {{0}}
set_instance_parameter_value cpu {{setting_HDLSimCachesCleared}} {{1}}
set_instance_parameter_value cpu {{setting_activateMonitors}} {{1}}
set_instance_parameter_value cpu {{setting_activateTestEndChecker}} {{0}}
set_instance_parameter_value cpu {{setting_activateTrace}} {{0}}
set_instance_parameter_value cpu {{setting_allow_break_inst}} {{0}}
set_instance_parameter_value cpu {{setting_alwaysEncrypt}} {{1}}
set_instance_parameter_value cpu {{setting_asic_add_scan_mode_input}} {{0}}
set_instance_parameter_value cpu {{setting_asic_enabled}} {{0}}
set_instance_parameter_value cpu {{setting_asic_synopsys_translate_on_off}} {{0}}
set_instance_parameter_value cpu {{setting_asic_third_party_synthesis}} {{0}}
set_instance_parameter_value cpu {{setting_avalonDebugPortPresent}} {{0}}
set_instance_parameter_value cpu {{setting_bhtPtrSz}} {{8}}
set_instance_parameter_value cpu {{setting_bigEndian}} {{0}}
set_instance_parameter_value cpu {{setting_branchpredictiontype}} {{Dynamic}}
set_instance_parameter_value cpu {{setting_breakslaveoveride}} {{0}}
set_instance_parameter_value cpu {{setting_clearXBitsLDNonBypass}} {{1}}
set_instance_parameter_value cpu {{setting_dc_ecc_present}} {{1}}
set_instance_parameter_value cpu {{setting_disable_tmr_inj}} {{0}}
set_instance_parameter_value cpu {{setting_disableocitrace}} {{0}}
set_instance_parameter_value cpu {{setting_dtcm_ecc_present}} {{1}}
set_instance_parameter_value cpu {{setting_ecc_present}} {{0}}
set_instance_parameter_value cpu {{setting_ecc_sim_test_ports}} {{0}}
set_instance_parameter_value cpu {{setting_exportHostDebugPort}} {{0}}
set_instance_parameter_value cpu {{setting_exportPCB}} {{0}}
set_instance_parameter_value cpu {{setting_export_large_RAMs}} {{0}}
set_instance_parameter_value cpu {{setting_exportdebuginfo}} {{0}}
set_instance_parameter_value cpu {{setting_exportvectors}} {{0}}
set_instance_parameter_value cpu {{setting_fast_register_read}} {{0}}
set_instance_parameter_value cpu {{setting_ic_ecc_present}} {{1}}
set_instance_parameter_value cpu {{setting_interruptControllerType}} {{Internal}}
set_instance_parameter_value cpu {{setting_itcm_ecc_present}} {{1}}
set_instance_parameter_value cpu {{setting_mmu_ecc_present}} {{1}}
set_instance_parameter_value cpu {{setting_oci_export_jtag_signals}} {{0}}
set_instance_parameter_value cpu {{setting_oci_version}} {{1}}
set_instance_parameter_value cpu {{setting_preciseIllegalMemAccessException}} {{0}}
set_instance_parameter_value cpu {{setting_removeRAMinit}} {{0}}
set_instance_parameter_value cpu {{setting_rf_ecc_present}} {{1}}
set_instance_parameter_value cpu {{setting_shadowRegisterSets}} {{0}}
set_instance_parameter_value cpu {{setting_showInternalSettings}} {{0}}
set_instance_parameter_value cpu {{setting_showUnpublishedSettings}} {{0}}
set_instance_parameter_value cpu {{setting_support31bitdcachebypass}} {{1}}
set_instance_parameter_value cpu {{setting_tmr_output_disable}} {{0}}
set_instance_parameter_value cpu {{setting_usedesignware}} {{0}}
set_instance_parameter_value cpu {{shift_rot_impl}} {{1}}
set_instance_parameter_value cpu {{tightly_coupled_data_master_0_paddr_base}} {{0}}
set_instance_parameter_value cpu {{tightly_coupled_data_master_0_paddr_size}} {{0.0}}
set_instance_parameter_value cpu {{tightly_coupled_data_master_1_paddr_base}} {{0}}
set_instance_parameter_value cpu {{tightly_coupled_data_master_1_paddr_size}} {{0.0}}
set_instance_parameter_value cpu {{tightly_coupled_data_master_2_paddr_base}} {{0}}
set_instance_parameter_value cpu {{tightly_coupled_data_master_2_paddr_size}} {{0.0}}
set_instance_parameter_value cpu {{tightly_coupled_data_master_3_paddr_base}} {{0}}
set_instance_parameter_value cpu {{tightly_coupled_data_master_3_paddr_size}} {{0.0}}
set_instance_parameter_value cpu {{tightly_coupled_instruction_master_0_paddr_base}} {{0}}
set_instance_parameter_value cpu {{tightly_coupled_instruction_master_0_paddr_size}} {{0.0}}
set_instance_parameter_value cpu {{tightly_coupled_instruction_master_1_paddr_base}} {{0}}
set_instance_parameter_value cpu {{tightly_coupled_instruction_master_1_paddr_size}} {{0.0}}
set_instance_parameter_value cpu {{tightly_coupled_instruction_master_2_paddr_base}} {{0}}
set_instance_parameter_value cpu {{tightly_coupled_instruction_master_2_paddr_size}} {{0.0}}
set_instance_parameter_value cpu {{tightly_coupled_instruction_master_3_paddr_base}} {{0}}
set_instance_parameter_value cpu {{tightly_coupled_instruction_master_3_paddr_size}} {{0.0}}
set_instance_parameter_value cpu {{tmr_enabled}} {{0}}
set_instance_parameter_value cpu {{tracefilename}} {{}}
set_instance_parameter_value cpu {{userDefinedSettings}} {{}}

add_instance jtag_uart altera_avalon_jtag_uart 18.1
set_instance_parameter_value jtag_uart {{allowMultipleConnections}} {{0}}
set_instance_parameter_value jtag_uart {{hubInstanceID}} {{0}}
set_instance_parameter_value jtag_uart {{readBufferDepth}} {{64}}
set_instance_parameter_value jtag_uart {{readIRQThreshold}} {{8}}
set_instance_parameter_value jtag_uart {{simInputCharacterStream}} {{}}
set_instance_parameter_value jtag_uart {{simInteractiveOptions}} {{NO_INTERACTIVE_WINDOWS}}
set_instance_parameter_value jtag_uart {{useRegistersForReadBuffer}} {{0}}
set_instance_parameter_value jtag_uart {{useRegistersForWriteBuffer}} {{0}}
set_instance_parameter_value jtag_uart {{useRelativePathForSimFile}} {{0}}
set_instance_parameter_value jtag_uart {{writeBufferDepth}} {{64}}
set_instance_parameter_value jtag_uart {{writeIRQThreshold}} {{8}}

add_instance led_pio altera_avalon_pio 18.1
set_instance_parameter_value led_pio {{bitClearingEdgeCapReg}} {{0}}
set_instance_parameter_value led_pio {{bitModifyingOutReg}} {{0}}
set_instance_parameter_value led_pio {{captureEdge}} {{0}}
set_instance_parameter_value led_pio {{direction}} {{Output}}
set_instance_parameter_value led_pio {{edgeType}} {{RISING}}
set_instance_parameter_value led_pio {{generateIRQ}} {{0}}
set_instance_parameter_value led_pio {{irqType}} {{LEVEL}}
set_instance_parameter_value led_pio {{resetValue}} {{0.0}}
set_instance_parameter_value led_pio {{simDoTestBenchWiring}} {{0}}
set_instance_parameter_value led_pio {{simDrivenValue}} {{0.0}}
set_instance_parameter_value led_pio {{width}} {{8}}

add_instance sdram altera_avalon_new_sdram_controller 18.1
set_instance_parameter_value sdram {{TAC}} {{5.5}}
set_instance_parameter_value sdram {{TMRD}} {{3.0}}
set_instance_parameter_value sdram {{TRCD}} {{20.0}}
set_instance_parameter_value sdram {{TRFC}} {{70.0}}
set_instance_parameter_value sdram {{TRP}} {{20.0}}
set_instance_parameter_value sdram {{TWR}} {{14.0}}
set_instance_parameter_value sdram {{casLatency}} {{3}}
set_instance_parameter_value sdram {{columnWidth}} {{8}}
set_instance_parameter_value sdram {{dataWidth}} {{16}}
set_instance_parameter_value sdram {{generateSimulationModel}} {{0}}
set_instance_parameter_value sdram {{initNOPDelay}} {{0.0}}
set_instance_parameter_value sdram {{initRefreshCommands}} {{2}}
set_instance_parameter_value sdram {{masteredTristateBridgeSlave}} {{0}}
set_instance_parameter_value sdram {{model}} {{single_Micron_MT48LC4M32B2_7_chip}}
set_instance_parameter_value sdram {{numberOfBanks}} {{4}}
set_instance_parameter_value sdram {{numberOfChipSelects}} {{1}}
set_instance_parameter_value sdram {{pinsSharedViaTriState}} {{0}}
set_instance_parameter_value sdram {{powerUpDelay}} {{100.0}}
set_instance_parameter_value sdram {{refreshPeriod}} {{15.625}}
set_instance_parameter_value sdram {{registerDataIn}} {{1}}
set_instance_parameter_value sdram {{rowWidth}} {{12}}

add_instance sys_clk_timer altera_avalon_timer 18.1
set_instance_parameter_value sys_clk_timer {{alwaysRun}} {{0}}
set_instance_parameter_value sys_clk_timer {{counterSize}} {{32}}
set_instance_parameter_value sys_clk_timer {{fixedPeriod}} {{0}}
set_instance_parameter_value sys_clk_timer {{period}} {{1}}
set_instance_parameter_value sys_clk_timer {{periodUnits}} {{MSEC}}
set_instance_parameter_value sys_clk_timer {{resetOutput}} {{0}}
set_instance_parameter_value sys_clk_timer {{snapshot}} {{1}}
set_instance_parameter_value sys_clk_timer {{timeoutPulseOutput}} {{0}}
set_instance_parameter_value sys_clk_timer {{watchdogPulse}} {{2}}

add_instance sysid altera_avalon_sysid_qsys 18.1
set_instance_parameter_value sysid {{id}} {{0}}

# exported interfaces
add_interface clk clock sink
set_interface_property clk EXPORT_OF clk_0.clk_in
add_interface led_pio_external_connection conduit end
set_interface_property led_pio_external_connection EXPORT_OF led_pio.external_connection
add_interface new_sdram_controller_0_wire conduit end
set_interface_property new_sdram_controller_0_wire EXPORT_OF sdram.wire
add_interface reset reset sink
set_interface_property reset EXPORT_OF clk_0.clk_in_reset

# connections and connection parameters
add_connection clk_0.clk cpu.clk

add_connection clk_0.clk jtag_uart.clk

add_connection clk_0.clk led_pio.clk

add_connection clk_0.clk sdram.clk

add_connection clk_0.clk sys_clk_timer.clk

add_connection clk_0.clk sysid.clk

add_connection clk_0.clk_reset cpu.reset

add_connection clk_0.clk_reset jtag_uart.reset

add_connection clk_0.clk_reset led_pio.reset

add_connection clk_0.clk_reset sdram.reset

add_connection clk_0.clk_reset sys_clk_timer.reset

add_connection clk_0.clk_reset sysid.reset

add_connection cpu.data_master cpu.debug_mem_slave
set_connection_parameter_value cpu.data_master/cpu.debug_mem_slave arbitrationPriority {{1}}
set_connection_parameter_value cpu.data_master/cpu.debug_mem_slave baseAddress {{0x01040800}}
set_connection_parameter_value cpu.data_master/cpu.debug_mem_slave defaultConnection {{0}}

add_connection cpu.data_master jtag_uart.avalon_jtag_slave
set_connection_parameter_value cpu.data_master/jtag_uart.avalon_jtag_slave arbitrationPriority {{1}}
set_connection_parameter_value cpu.data_master/jtag_uart.avalon_jtag_slave baseAddress {{0x01041038}}
set_connection_parameter_value cpu.data_master/jtag_uart.avalon_jtag_slave defaultConnection {{0}}

add_connection cpu.data_master led_pio.s1
set_connection_parameter_value cpu.data_master/led_pio.s1 arbitrationPriority {{1}}
set_connection_parameter_value cpu.data_master/led_pio.s1 baseAddress {{0x01041020}}
set_connection_parameter_value cpu.data_master/led_pio.s1 defaultConnection {{0}}

add_connection cpu.data_master sdram.s1
set_connection_parameter_value cpu.data_master/sdram.s1 arbitrationPriority {{1}}
set_connection_parameter_value cpu.data_master/sdram.s1 baseAddress {{0x00800000}}
set_connection_parameter_value cpu.data_master/sdram.s1 defaultConnection {{0}}

add_connection cpu.data_master sys_clk_timer.s1
set_connection_parameter_value cpu.data_master/sys_clk_timer.s1 arbitrationPriority {{1}}
set_connection_parameter_value cpu.data_master/sys_clk_timer.s1 baseAddress {{0x01041000}}
set_connection_parameter_value cpu.data_master/sys_clk_timer.s1 defaultConnection {{0}}

add_connection cpu.data_master sysid.control_slave
set_connection_parameter_value cpu.data_master/sysid.control_slave arbitrationPriority {{1}}
set_connection_parameter_value cpu.data_master/sysid.control_slave baseAddress {{0x01041030}}
set_connection_parameter_value cpu.data_master/sysid.control_slave defaultConnection {{0}}

add_connection cpu.instruction_master cpu.debug_mem_slave
set_connection_parameter_value cpu.instruction_master/cpu.debug_mem_slave arbitrationPriority {{1}}
set_connection_parameter_value cpu.instruction_master/cpu.debug_mem_slave baseAddress {{0x01040800}}
set_connection_parameter_value cpu.instruction_master/cpu.debug_mem_slave defaultConnection {{0}}

add_connection cpu.instruction_master sdram.s1
set_connection_parameter_value cpu.instruction_master/sdram.s1 arbitrationPriority {{1}}
set_connection_parameter_value cpu.instruction_master/sdram.s1 baseAddress {{0x00800000}}
set_connection_parameter_value cpu.instruction_master/sdram.s1 defaultConnection {{0}}

add_connection cpu.irq jtag_uart.irq
set_connection_parameter_value cpu.irq/jtag_uart.irq irqNumber {{16}}

add_connection cpu.irq sys_clk_timer.irq
set_connection_parameter_value cpu.irq/sys_clk_timer.irq irqNumber {{1}}

# interconnect requirements
set_interconnect_requirement {{$system}} {{qsys_mm.clockCrossingAdapter}} {{HANDSHAKE}}
set_interconnect_requirement {{$system}} {{qsys_mm.enableEccProtection}} {{FALSE}}
set_interconnect_requirement {{$system}} {{qsys_mm.insertDefaultSlave}} {{FALSE}}
set_interconnect_requirement {{$system}} {{qsys_mm.maxAdditionalLatency}} {{1}}

save_system {{first_nios2_system.qsys}}

""");

with open(qp + '/first_nios2_system.tcl', 'w') as f:
    f.write(first_nios2_system)
