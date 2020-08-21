# 2178

import sys

class mazeProbe():
    
    def __init__(self, n, m):
        self.N = n
        self.M = m
        self.maze = []
        self.queue = []
        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, -1, 1]
    
    def insertLists(self):
        for _ in range(self.N):
            self.maze.append(list(sys.stdin.readline()))
        
    def getAnswer(self):
        self.queue = [[0, 0]]
        self.maze[0][0] = 1
        
        while self.queue:
            a, b = self.queue[0][0], self.queue[0][1]
            del self.queue[0]
            
            for i in range(4):
                x = a + self.dx[i]
                y = b + self.dy[i]
                
                if 0 <= x < self.N and 0 <= y < self.M and self.maze[x][y] == '1':
                    self.queue.append([x, y])
                    self.maze[x][y] = self.maze[a][b] + 1
         
        print(self.maze[self.N -1][self.M - 1])
        
        
n, m = map(int, sys.stdin.readline().split())
mazeprobe = mazeProbe(n, m)
mazeprobe.insertLists()
mazeprobe.getAnswer()
