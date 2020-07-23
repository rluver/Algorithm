#2751

n = int(input())

solution = [int(input()) for _ in range(n)]

solution = sorted(solution)

for i in solution:
    print(i)

    
    
# 11650

n = int(input())

solution = [list(map(int, input().split())) for _ in range(n)]

solution.sort(key = lambda x: (x[0], x[1]))

for coord in solution:
    print(coord[0], coord[1])

    
    
# 11651

n = int(input())

solution = [list(map(int, input().split())) for _ in range(n)]

solution.sort(key = lambda x: (x[1], x[0]))

for coord in solution:
    print(coord[0], coord[1])
    
    
    
# 10814

n = int(input())

solution = [list(input().split()) for _ in range(n)]

solution.sort(key = lambda x: int(x[0]))

for value in solution:
    print(value[0], value[1])
    
    
    
# 10825

n = int(input())

solution = [list(input().split()) for _ in range(n)]

solution.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for value in solution:
    print(value[0])
    
