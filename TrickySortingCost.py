def sortingCost(N, arr):
    # code here
    hashmap = {}
    max = 1
    for i in arr:
        if i - 1 in hashmap:
            hashmap[i] = hashmap[i - 1] + 1
            if max < hashmap[i]:
                max = hashmap[i]
        else:
            hashmap[i] = 1

    return N - max

