# 2869

import sys


class wantGoUp():
    
    def __init__(self, A, B, V):
        self.A = A
        self.B = B
        self.V = V
        
        self.takenTime = (self.V - self.B) / (self.A - self.B)
        self.result = 0
    
    def getDays(self):
        if self.takenTime == int(self.takenTime):
            self.takenTime = int(self.takenTime)
        else:
            self.takenTime = int(self.takenTime) + 1
    
    def showResult(self):
        print(self.takenTime)
        
        
a,b,v = map(int, sys.stdin.readline().split())
wantgoup = wantGoUp(a, b, v)
wantgoup.getDays()
wantgoup.showResult()



# 1654

class LanDivide:
    
    def __init__(self, K, N):
        self.K = K
        self.N = N
        self.LAN = []
        
        self.start = 1
        self.end = 0
    
    def getMaxLen(self):
        [self.LAN.append(int(input())) for _ in range (self.K)]
        self.end = max(self.LAN)
                
        while self.start <= self.end:
            med = (self.start + self.end) // 2
            num = 0        
            
            for i in self.LAN:
                num += i // med
        
            if num >= self.N:
                self.start = med + 1
            else:
                self.end = med - 1

K, N = map(int, input().split())
landiv = LanDivide(K, N)
landiv.getMaxLen()
print(landiv.end)
