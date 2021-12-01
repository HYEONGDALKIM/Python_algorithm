# 더하기 사이클 

N = int(input())
Num = N
cnt = 0 

while True:
    a = Num//10 
    b = Num%10
    c  = (a+b)%10
    Num = (b*10)+c
    cnt = cnt + 1
    
    if(Num == N): 
        break
print(cnt)