import math
def maxPoints(points):
    hashmap = {}  # consists of slope, occurence of slope
    # slope is m; y = mx+c where m is (y2-y1)/(x2-x1)
    if len(points) <= 0:
        return 0
    if len(points)==2:
        return 2
    else:
        max = 1

        for j in range(0,len(points)-1):
            x1 = points[j][0]
            y1 = points[j][1]
            hashmap={}
            for i in range(j+1, len(points)):
                if points[i][0] == x1:
                    m = math.inf
                else:
                    m = (points[i][1] - y1) / (points[i][0] - x1)

                if m in hashmap.keys():
                    hashmap[m] = hashmap[m] + 1
                    if max < hashmap[m]:
                        max = hashmap[m]
                else:
                    hashmap[m] = 1
        return max + 1

points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
print(maxPoints(points))