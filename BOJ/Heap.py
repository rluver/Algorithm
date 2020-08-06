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



# 11279

import sys
import heapq


class MaxHeap:
    
    def __init__(self, N):
        self.N = N
        self.heap = []
    
    def insertNum(self):
        self.num = int(sys.stdin.readline())
        
        return self.num
        
    def getMaxHeap(self):        
        for _ in range(self.N):
            if self.insertNum() != 0:
                heapq.heappush(self.heap, -self.num)
            else:
                if self.heap:
                    print(-1 * heapq.heappop(self.heap))
                else:
                    print(0)

minheap = MaxHeap(int(input()))
minheap.getMaxHeap()
