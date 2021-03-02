from typing import List, Any

file = open('asks9.txt', 'r')
N=0
k=0
while 1:
    k=k+1
    # read by character
    char = file.read(1)
    if not char:
        break
    s=ord(char)
    if s%2==1:
        N=N+1
        B=list(char)

for i in range(N):
    pl=0
    for j in range(N):
        if B[i]==B[j]:
            pl=pl+1
    num = round(pl //k) + 1
    for w in range(num):
        var = B[i] == "*"
    print(B[i])
file.close()
