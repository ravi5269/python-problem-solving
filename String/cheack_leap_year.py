# How to check if a given year is a leap year? (solution)
def check_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True  
    else:
        return False  
    
        
year = 2024
if check_year(year):
    print("Leap Year",year)
else:
    print("Not a Leap Year",year)