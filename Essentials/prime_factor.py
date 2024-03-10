# How to find all prime factors of a given number? (solution)
def prime_factor(num):
    temp = num
    i=2
    while temp>1:
        if temp%i==0:
            print(i,end=", ")
            temp=int(temp/i)
        else:
            i = i+1
num = 45
print(prime_factor(num))
