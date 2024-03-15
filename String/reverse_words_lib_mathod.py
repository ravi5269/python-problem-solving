# How do you reverse words in a given sentence without using any library method? (solution)

def reverse_word(string):
    rever_word = string[::-1]
    return rever_word
word = "hello"
print("Reverse Word is :" ,reverse_word(word))