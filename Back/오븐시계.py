A,B=input().split()
A=int(A)
B=int(B)
C=int(input())
total=A*60+B+C
if total>=24*60: total-=24*60
A=int(total/60)
B=total%60
print(str(A)+" "+str(B))
