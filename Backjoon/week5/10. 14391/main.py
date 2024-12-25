n, m = map(int, input().split())
paper = [list(map(int, input())) for _ in range(n)]

def rip_paper():
    answer = 0
  
    for bitmask in range(1 << (n * m)):
        total = 0
        for i in range(n):
            sum1 = 0
            for j in range(m):
                idx = i * m + j
                if bitmask & (1 << idx) != 0:
                    sum1 = sum1 * 10 + paper[i][j]
                else:
                    total += sum1
                    sum1 = 0
            total += sum1
        
        for j in range(m):
            sum2 = 0
            for i in range(n):
                idx = i * m + j
                if bitmask & (1 << idx) == 0:
                    sum2 = sum2 * 10 + paper[i][j]
                else:
                    total += sum2
                    sum2 = 0
            total += sum2
        answer = max(answer, total)
    return answer
    
print(rip_paper())