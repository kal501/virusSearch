import magic

m = magic.open(magic.MAGIC_NONE)
m.load()
ftype = m.file(r"log.exe")
print(ftype)
