# How to print a given Pyramid structure? (solution)
print("Half Pyramid Pattern of Stars (*):")
for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print()


print("Full Pyramid Pattern of Star (*):")
for i in range(5):

    for j in range(-6,-i):
        print(" ",end = "")
    for k in range(i+1):
        print("* ",end="")
    print()

print("pattern of numbers")
num =1 
for i in range(5):
    for j in range(i+1):
        print(num, end=" ")
        num = num+1
    print()


