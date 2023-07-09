# Maximum consecutive one’s (or zeros) in a binary array
def maxCount(arr):
    count = 0
    maxCount = 0
    for i in arr:
        if i is 1:
            count = count+1
        if i is 0:
            count=0

        if count > maxCount:
            maxCount = count
        # print(count, maxCount)
    return maxCount

arr = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]
print(maxCount(arr))