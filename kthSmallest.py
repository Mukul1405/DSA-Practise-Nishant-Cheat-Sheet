def kthSmallest(matrix, k: int) -> int:
    if k is 0:
        return -1
    if k is 1:
        return matrix[0][0]
    arr = []
    for i in matrix:
        for j in i:
            arr.append(j)

    arr.sort()
    return arr[k - 1]