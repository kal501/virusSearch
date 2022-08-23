import idautils
import idc

for addr, name in idautils.Names():
    if "CreateFile" in name:
        print(hex(addr),name)
        
  
ea = idc.get_name_ea_simple("CreateFileA")
if ea != idaapi.BADADDR:
    print(hex(ea), idc.generate_disasm_line(ea,0))

else:
    print("Not Found")
    