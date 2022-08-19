import hashlib
content = open(r"log.exe", "rb").read()
print(hashlib.md5(content).hexdigest())
print(hashlib.sha256(content).hexdigest())
print(hashlib.sha1(content).hexdigest())