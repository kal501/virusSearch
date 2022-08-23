import idc
import idautils

ea = idc.get_name_ea_simple("CreateFileA")
if ea != idaapi.BADADDR:
    for ref in idautils.CodeRefsTo(ea, 1):
        print(hex(ref), idc.generate_disasm_line(ref,0))
        
