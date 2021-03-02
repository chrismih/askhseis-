print("Dwse diastash")
N = input()
N = int(N)
if N% 2 == 0:
    num = N ** 2 // 2
    A = [0 for i in range(N ** 2 // 2)]
    thislist = [1 for j in range(num)]
    B = thislist + A

else:
    num = round(N ** 2 / 2) + 1
    A = [0 for i in range(N ** 2 // 2)]
    thislist = [1 for j in range(num)]
    B = thislist + A


s1=0
s2=0
s3=0
S=0
for w in range(100):
    S = S + s1 + s2 + s3
    import random
    random.shuffle(B)
    k=0
    for i in range(N):
        B[i]=B[k:k + N]
        #print(B[i])
        k = k + N




    x=0
    s1=0

    for i in range(N+1):
        l = (2 - 3)
        for j in range(N+1):
            l=l+1
            if x>=4:
                s1=s1+1
        if B[l]==1 and B[l+1]==1:
                x=x+1
        else:
                x=0
    t=0
    s2=0
    for a in range(N+1):
        k=(2-3)
        for b in range(N+1):
            k=k+1
            if t>=4:
                s2=s2+1
        if B[k]==1 and B[k+N]==1:
            t=t+1
        else:
            t=0
    m=0
    s3=0
    for c in range(N+1):
        f=(2-3)
        for d in range(N+1):
            f=f+1
            if m>=4:
                s3=s3+1
        if B[f]==1 and B[f+N+1]==1:
            m=m+1
        else:
            m=0




S=S/100


print(S)



