# How do you check if two strings are a rotation of each other? (solution)

def are_rotations(s1, s2):
    if len(s1) != len(s2):
        return True
    
    concatenated = s1 + s1
    return s2 in concatenated

s1 = "abcdq"
s2 = "cdqab"
print("Are the strings rotations of each other?", are_rotations(s1, s2))
