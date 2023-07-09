s1 = "abc"
s2 = "cba"

hashmap1 = {}
hashmap2 = {}

for i in s1:
    hashmap1[i] = 1

hashmap1['d']=0
hashmap1.pop('d',hashmap1['d'])

for i in s2:
    hashmap2[i] = 1

print(hashmap1,hashmap2)

print(hashmap1['d'])