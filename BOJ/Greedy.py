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
