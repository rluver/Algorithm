# 1181

import sys

def wordSorting():
    
    wordLists = []
    wordNum = int(sys.stdin.readline())
        
    for _ in range(wordNum):
        wordLists.append(sys.stdin.readline())
            
    wordLists = set(wordLists)
    wordLists = list(map(lambda x: [len(x), x], wordLists))    
    wordLists.sort()
            
    for _, word in wordLists:
        print(word)
    
    
wordSorting()
