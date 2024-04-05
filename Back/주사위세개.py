A,B,C=input().split()
A=int(A)
B=int(B)
C=int(C)
M=max(A,B,C)
if A==B:
    if B==C:
        print(10000+A*1000)
    else:
        print(1000+A*100)
else:
    if B==C:
        print(1000+B*100)
    elif A==C:
        print(1000+C*100)
    else:
        print(M*100)


