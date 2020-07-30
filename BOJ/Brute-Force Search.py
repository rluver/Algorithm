# 1476

class YearCalculation:
    
    def __init__(self, E, S, M):        
        self.E = E
        self.S = S
        self.M = M
        self.YEAR = 1
    
    def CalculateYear(self):
        while True:
            if (self.YEAR - self.E) % 15 == 0 and (self.YEAR - self.S) % 28 == 0 and (self.YEAR - self.M) % 19 == 0:
                print(self.YEAR)
                break
            self.YEAR += 1

E, S, M = map(int, input().split())
yearcal = YearCalculation(E, S, M)
yearcal.CalculateYear()
