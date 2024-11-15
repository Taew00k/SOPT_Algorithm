import sys
input = sys.stdin.readline

num = 1
movie = 0
N = int(input())

while True:
    if '666' in str(num):
        movie = movie + 1
    
    if  N == movie:
        print(num)
        break;   
    
    num = num+1    