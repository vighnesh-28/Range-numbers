n=int(input())    #5
l=[]
for i in range(n): # 0 1 2 3 4
    l.append(int(input()))
psum=0
nsum=0
zsum=0
for i in l:
    if i>0:
        psum=psum+i
    elif i<0:
        nsum=nsum+i
    else:
        zsum=zsum+i
print(psum/n)
output:
    10//2
    5
    10%2
    0
    10/2
    5.0
