import math

def prime_number(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(number))+ 1, 2):
            if number % i==0:
                return False
        return True
        

number = int(input("Enter a number:"))

if prime_number(number):
    print(number ,"is a prime number ")

else:
    print(number,"is not a prime number")