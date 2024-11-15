import sys
input = sys.stdin.readline

t1,t2=0,0
tmp1,tmp2=0,0
s=0

for i in range(int(input())):
    
  team,time=input().split()
  m,sec=map(int, time.split(':'))
  t=60*m+sec
  
  if team=='1':
    if s==0:
      s+=1
      tmp1=t
    elif s!=0:
      s+=1
      if s==0:
        t2+=t-tmp2  
  else:
    if s==0:
      s-=1
      tmp2=t
    elif s!=0:
      s-=1
      if s==0:
        t1+=t-tmp1  
        
if s>0:
  t1+=60*48-tmp1
elif s<0:
  t2+=60*48-tmp2
  
print('{:0>2}:{:0>2}'.format((t1)//60,t1%60))
print('{:0>2}:{:0>2}'.format((t2)//60,t2%60))