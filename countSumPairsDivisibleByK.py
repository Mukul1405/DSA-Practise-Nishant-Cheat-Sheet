def countPairsDivisibleByK(arr,k):
    hashmap = {}  # we will store remainder and their occurences
    ans=0
    for i in arr:
        if i%k in hashmap.keys():
            hashmap[i%k] = hashmap[i%k]+1
        else:
            hashmap[i%k]=1

        if k-(i%k) in hashmap.keys():
            if k - (i % k) == i % k:
                ans = ans + hashmap[i % k] - 1
            else:
                ans = ans+hashmap[k-(i%k)]

    return ans
arr=[2,2,1,7,5,3]
k = 4
print(countPairsDivisibleByK(arr,k))