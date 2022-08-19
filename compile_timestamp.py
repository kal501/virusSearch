import time
import pefile

pe = pefile.PE("[target file]")
timestamp = pe.FILE_HEADER.TimeDateStamp
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp)))
