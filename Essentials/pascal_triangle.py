# How to print Pascal’s triangle? (solution)
row = 6
k=1
for i in range(1,row+1):
    for a in range(1,(row-i)+1):
        print(" ",end="")
    for j in range(0,i):
        if j==0 or i ==0:
            k=1
        else:
            k=k*(i-j)//j
        print(k,end=" ")
    print()