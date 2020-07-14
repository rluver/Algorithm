#1463

n = int(input())

solution = [0 for _ in range(n + 1)]

for i in range(2, n + 1):
    
    solution[i] = solution[i - 1] + 1
    
    if i % 2 == 0 and solution[i] > solution[i // 2] + 1:
        solution[i] = solution[i // 2] + 1
        
    if i % 3 == 0 and solution[i] > solution[i // 3] + 1:
        solution[i] = solution[i // 3] + 1
        
print(solution[n])



#11726

n = int(input())

solution = [0 for _ in range(1001)]

solution[1] = 1
solution[2] = 2
for i in range(3, n + 1):
    
    solution[i] = (solution[i - 1] + solution[i - 2] ) % 10007
    
print(solution[n] % 10007)



#11727

n = int(input())

solution = [0 for _ in range(1001)]

solution[1] = 1
solution[2] = 3
for i in range(3, n + 1):
    
    solution[i] = (solution[i - 1] + 2 * solution[i - 2] ) % 10007
    
print(solution[n] % 10007)



#9095

n = int(input())

solution = [0 for _ in range(n + 1)]

solution[1] = 1
solution[2] = 2
solution[3] = 4
for i in range(4, n + 1):
    
    solution[i] = solution[i - 3] + solution[i - 2] + solution[i - 1]

print(solution[n])



#10844

n = int(input())

solution = [[0] * 10 for j in range(n + 1)]

for i in range(1, 10):
    solution[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            solution[i][j] = solution[i - 1][1]
        elif j == 9:
            solution[i][j] = solution[i - 1][8]
        else:
            solution[i][j] = solution[i - 1][j - 1] + solution[i - 1][j + 1]
            
print(sum(solution[n]) % 1000000000)



#11057

n = int(input())

solution = [[0] * 10 for _ in range(n + 1)]
solution[1] = [1 for _ in range(10)]

for i in range(2, n + 1):
    for j in range(10):
        for k in range(j + 1):
            solution[i][j] += solution[i - 1][k]
            
print(sum(solution[n]) % 10007)
