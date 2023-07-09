def k_anagram(str1,str2,k):
    hashmap1={}
    hashmap2={}
    for i in str1:
        if i in hashmap1.keys():
            hashmap1[i]=hashmap1[i]+1
        else:
            hashmap1[i]=1

    for i in str2:
        if i in hashmap2.keys():
            hashmap2[i]=hashmap2[i]+1
        else:
            hashmap2[i]=1

    count = 0
    for i in hashmap1.keys():
        if i in hashmap2.keys():
            if hashmap1[i]>hashmap2[i]:
                count = count+hashmap2[i]
            else:
                count = count+hashmap1[i]

    print(count)
    if len(str1) >= len(str2):
        if count+k>=len(str1):
            return True
    else:
        if count+k>=len(str2):
            return True

    return False


str1 = "anagram"
str2 = "grammar"
k = 3
print(k_anagram(str1,str2,k))