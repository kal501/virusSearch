import idc

idc.add_bpt(idc.get_screen_ea()) # breaking point set
idc.start_process('', '', '')
evt_code = idc.wait_for_next_event(WFNE_SUSP, -1) # event code
if evt_code > 0 and evt_code != idc.PROCESS_EXITED:
    evt_ea = idc.get_event_ea()
    print("Breaking Point Triggered at : ",hex(evt_ea),idc.generate_disasm_line(evt_ea,0))
