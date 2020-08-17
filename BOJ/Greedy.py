# 11399

import sys


class ATM():
    
    def __init__(self, n):
        self.N = n
        self.sum = 0
    
    def insertTime(self):
        self.timeLists = list(map(int, sys.stdin.readline().split()))
        
    def calculateMin(self):
        self.timeLists.sort()
        
        for i in range(self.N):
            for j in range(i + 1):
                self.sum += self.timeLists[j]
        
        print(self.sum)

        
atm = ATM(int(sys.stdin.readline()))
atm.insertTime()
atm.calculateMin()



# 11047

class Coin0:
    
    def __init__(self, N, K):
        self.N = N
        self.K = K
        self.M = []
        self.num = 0
    
    def getCoinNum(self):
        for i in range(N):
            self.M.append(int(input()))
        
        for i in range(self.N - 1, -1, -1):
            if self.K == 0:
                break;
            if self.M[i] > self.K:
                continue
            
            self.num += self.K // self.M[i]
            self.K %= self.M[i]

N, K = map(int, input().split())
coin = Coin0(N, K)
coin.getCoinNum()

print(coin.num)
