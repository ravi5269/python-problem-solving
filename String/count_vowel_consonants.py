# How do you count the number of vowels and consonants in a given string? (solution)
vowels_count = 0;  
consonants_count = 0;  
str = "This is a really simple sentence";  
   
#Converting entire string to lower case to reduce the comparisons  
str = str.lower();  
for i in range(0,len(str)):   
    if str[i] in ('a',"e","i","o","u"):  
        vowels_count = vowels_count + 1;  
    elif (str[i] >= 'a' and str[i] <= 'z'):  
        consonants_count= consonants_count + 1;  
print("Total number of vowel and consonant " );  
print("total vowels :",vowels_count);  
print("total consonants :",consonants_count);  