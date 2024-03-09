# How do you swap two numbers without using the third variable? (solution)
# use funcation
def swap_number(a,b):
    a = a+b
    b = a-b
    a= a-b
    return a,b

number1 = int(input("Enter the value of a = "))
number2 = int(input("Enter the value of b = "))

number1,number2 = swap_number(number1,number2)
print("After swapping number:")
print("a =",number1)
print("b =",number2)


# swapping 
x = int(input("Enter the value of x :"))
y = int(input("Enter the value of y :"))
print("Before swapping \n x =",x,'y=',y)

x,y = y,x
print("After swapping \n x =",x,'y=',y)
