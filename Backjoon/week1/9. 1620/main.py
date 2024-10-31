import sys
input = sys.stdin.readline

n, m = map(int, input().split())

book_num = {}
book_name = {}
for i in range(1,n+1):
    name = input().rstrip()
    book_num[i] = name
    book_name[name] = i

for j in range(m):
    data = input().rstrip()
    if data.isdigit():
        print(book_num[int(data)])
    else:
        print(book_name[data])