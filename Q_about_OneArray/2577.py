#숫자의 개수
A = int(input())
B = int(input())
C = int(input())

Number = list(str(A*B*C))

for i in range(10):
    print(Number.count(str(i)))