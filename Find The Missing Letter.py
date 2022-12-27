# print(find_missing_letter_in("abcdeghi"))  # f
# print(find_missing_letter_in("defgi"))  # h
# print(find_missing_letter_in("xyz"))  # No Missing Letter In Sequence

import string

def find_missing_letter_in(givenLetters):
     alpha = string.ascii_letters
     start = alpha.index(givenLetters[0])
     for letter in alpha[start:]:
        if letter not in givenLetters:
            return letter


     return f" No Missing Letter In Sequence"
     

print(find_missing_letter_in("abcdeghi"))  # f
print(find_missing_letter_in("defgi"))  # h
print(find_missing_letter_in("xz"))  # No Missing Letter In Sequence
