import pefile
pe = pefile.PE("[Target file]")
for section in pe.sections:
    print("%s\t%s" % (section.Name, section.get_hash_md5()))