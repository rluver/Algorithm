# 1927

import heapq


class MinHeap:
    
    def __init__(self, N):
        self.N = N
        self.heap = []
    
    def insertNum(self):
        self.num = int(input())
        
        return self.num
        
    def getMinHeap(self):        
        for _ in range(self.N):
            if self.insertNum() != 0:
                heapq.heappush(self.heap, self.num)
            else:
                if self.heap:
                    print(heapq.heappop(self.heap))
                else:
                    print(0)

minheap = MinHeap(int(input()))
minheap.getMinHeap()
