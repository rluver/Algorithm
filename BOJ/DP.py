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
