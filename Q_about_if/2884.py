H, M = map(int,input().split())

C_T = H*60 + M - 45

C_H = C_T // 60
C_M = C_T % 60

if 0 > C_H :
    print(C_H+24, C_M)
else :     
    print(C_H, C_M)