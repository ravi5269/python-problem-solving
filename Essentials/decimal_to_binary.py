# decimal to binary convert
def decimal_to_binary(decimal_number):
    binary_number = bin(decimal_number)
    return binary_number[2:]

#take input from the user 
decimal_number = int(input("Enter a decimal number :"))
binary_number = decimal_to_binary(decimal_number)

print("Binary number :",binary_number)


# using loop 
d = 0
bn = 0
a = 1
number = int(input("Enter a decimal number :"))
while number>0:
    d = number%2
    bn = bn+d*a
    a = a*10
    number=int(number/2)
print("Binary number is :",bn)