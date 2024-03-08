def is_palindrome(number):
    number_str = str(number)

    if number_str == number_str[::-1]:
        return True
    else:
        return False
    

number = int(input("Enter a number :"))

if is_palindrome(number):
    print(number,"is a palindrome")
else:
    print(number,"is not a palindrome")