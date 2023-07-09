def countSubArrays(arr):
    hashmap = {}
    sum,freq = 0,1
    hashmap[sum]=freq
    count = 0
    for i in arr:
        if i is 0:
            sum = sum-1
        else:
            sum = sum+1

        if sum in hashmap:
            hashmap[sum] = hashmap[sum]+1
            count = count+hashmap[sum]-1

        else:
            hashmap[sum]=freq
        # print(hashmap,count)
    return count

arr = [1, 0, 0, 1, 0, 1, 1]
print(countSubArrays(arr))