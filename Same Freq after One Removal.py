def samefreq(string):
    hashmap={}
    for i in string:
        if i in hashmap.keys():
            hashmap[i] = hashmap[i]+1
        else:
            hashmap[i]=1

    maxfreq = max(hashmap.values())
    minfreq = min(hashmap.values())
    if maxfreq-minfreq <=1:
        return True
    return False

string = "xxxxyyzz"
print(samefreq(string))