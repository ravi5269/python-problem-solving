# How do you remove a given character from String? (solution)
def remove_character(s, char):
    result = ""
    
    for c in s:
        
        if c != char:
            result += c
    
    return result


s = "ravikant"
char_to_remove = "a"
print("String after removing char:", remove_character(s, char_to_remove))
