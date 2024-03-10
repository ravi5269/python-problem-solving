# How to find the largest prime factor of a given integral number? (solution)
def largest_prime_factor(number):
    # Initialize the largest prime factor
    largest_factor = 0
    
    # Check divisibility by 2
    while number % 2 == 0:
        largest_factor = 2
        number = number // 2
    
    # Check divisibility by odd numbers starting from 3
    factor = 3
    while factor * factor <= number:
        while number % factor == 0:
            largest_factor = factor
            number = number // factor
        factor += 2  # Check the next odd number
    
    # If the remaining number is greater than 1, it is also a prime factor
    if number > 1:
        largest_factor = number
    
    return largest_factor

# Example usage
number = 144
print("Largest prime factor of", number, "is:", largest_prime_factor(number))

