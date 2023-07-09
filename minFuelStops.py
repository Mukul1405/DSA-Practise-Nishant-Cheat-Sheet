import queue
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations) -> int:
        if startFuel>=target:
            return 0

        if startFuel < stations[0][0]:
            return -1
        else:
            self.cur = startFuel
            self.pq = queue.PriorityQueue()
            self.i =0
            self.NumberOfStation = 0
            while(self.cur<target):
                while(self.i<len(stations) and self.cur>=stations[self.i][0]):
                    self.pq.put((stations[self.i][0]*-1,stations[self.i][1]))
                    self.i+=1
                    print("element added")
                    if self.i >=len(stations):
                        break
                if self.pq.empty():
                    # print("-21")
                    return -1
                else:
                    priority,val = self.pq.get()
                    self.cur = self.cur+val
                    self.NumberOfStation+=1
            return self.NumberOfStation
s = Solution()
print(s.minRefuelStops(130,10,[[10,60],[20,30],[30,30],[60,40]]))
# print(s.minRefuelStops(100,50,[[25,50],[50,25]]))
