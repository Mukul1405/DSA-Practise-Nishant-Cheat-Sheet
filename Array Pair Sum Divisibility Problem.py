def solution(arr,k):
    hashmap = {}  # we will store remainder and their occurences
    if len(arr)%2==1:
        return False
    for i in arr:
        if i % k in hashmap.keys():
            hashmap[i % k] = hashmap[i % k] + 1
        else:
            hashmap[i % k] = 1

        if k - (i % k) in hashmap.keys() and hashmap[k-(i%k)] > 0 and hashmap[i%k]>0:
            if i%k != k-(i%k):
                hashmap[i%k] = hashmap[i%k]-1
                hashmap[k-(i%k)]=hashmap[k-(i%k)]-1
            else:
                hashmap[i%k] = hashmap[i%k]-1
    if 0 in hashmap.keys():
        if hashmap[0]%2==0:
            hashmap[0]=0
        else:
            return False
    for i in hashmap.keys():
        print(i,hashmap[i])
    if max(hashmap.values())>0:
        return False
    return True

arr = [13,13,14,1]
k=2
print(solution(arr,k))