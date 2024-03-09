#use funcation to reverse a number
def reverse_interger(number):
    reverse_number = int(str(number)[::-1])
    return reverse_number

# take input from user 
number = int(input("Enter an integer :"))

reverse_number = reverse_interger(number)
print("Reverse integer is ",reverse_number)


# use loop to reverse number
i = int(input("Enter a number "))
reverse = 0 
while(i>0):
    reverse=(reverse*10)+ i%10
    i=i//10
print("Reverse number",reverse)
    