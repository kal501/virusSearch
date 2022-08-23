import ssdeep

hash1 = ssdeep.hash_from_file('jnas.exe')
print(hash1)

hash2 = ssdeep.hash_from_file('aiggs.exe')
print(hash2)

ssdeep.compare(hash1, hash2)

# 유사도 측정 
