H,M=input().split()
H=int(H)
M=int(M)
total=60*H+M
total-=45
if total<0: total=total+24*60
H=int(total/60)
M=total%60
print(str(H)+' '+str(M)) #파이썬에서는 숫자와 문자열을 직접 결합할 수 없음.