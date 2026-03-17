n=int(input())    #5
l=[]
for i in range(n): # 0 1 2 3 4
    l.append(int(input()))
psum=0
nsum=0
zsum=0
for i in l:  #[1,0,1,-1,-1]
    if i>0:
        psum=psum+i
    elif i<0:
        nsum=nsum+i
    else:
        zsum=zsum+i
print("%.2f"%(psum/n))
print("%f"%(nsum/n))
print("%f"%(zsum/n))
output:
5
1
0
1
-1
-1
0.400000
-0.400000
0.000000
