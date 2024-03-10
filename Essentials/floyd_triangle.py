# How to print Floyd’s triangle? (solution)
rows = 5
k=1 
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(k,end=" ")
        k += 1
    print()