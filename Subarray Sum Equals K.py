
## Optimal approcah usinf prefix and suffix concept
def subArraySumEqualsK(arr,k):
    hashmap = {}
    sum = 0
    freq = 1
    count = 0
    hashmap[sum] = freq
    for i in arr:
        sum = sum+i
        if sum not in hashmap.keys():
            hashmap[sum] = freq
        else:
            hashmap[sum] = hashmap[sum]+1
        if sum-k in hashmap.keys():
            count = count+hashmap[sum-k]
        # print(hashmap,count)
    return count

print(subArraySumEqualsK([1,2,3],3))
