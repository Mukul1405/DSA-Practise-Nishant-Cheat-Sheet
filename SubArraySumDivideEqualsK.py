
def subArraySumDivideEqualsK(arr,k):
    hashmap={}
    sum = 0
    remainder = 0
    freq = 1
    count = 0
    hashmap[remainder] = freq
    for i in arr:
        sum=sum+i
        while(sum<0):
            sum = sum+k
        remainder = sum%k
        if remainder in hashmap:
            hashmap[remainder] = hashmap[remainder]+1
            count = count + hashmap[remainder]-1
        else:
            hashmap[remainder] = freq

    return count
arr = [4, 5, 0, -2, -3, 1]
print(subArraySumDivideEqualsK(arr,5))