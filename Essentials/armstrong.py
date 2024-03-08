def is_armstrong(number):
    # Convert the number to a string to count the number of digits
    num_str = str(number)
    num_digits = len(num_str)

    sum_of_digits = sum(int(digit)** num_digits for digit in num_str)

    return sum_of_digits == number

number = int(input("Enter a number: "))
if is_armstrong(number):
    print(number,"is an armstong number")
else:
    print(number,"is not an armstrong number")



