# Find Longest Word in a String

def longest_word_in(sentence):
  count = 0
  words = sentence.split(' ')
  for word in words:
    if len(word) > count:
         count= len(word)  
         longest = word
  return longest

# print(len(word))
# Testing Ouput
print (longest_word_in("In Programming We Love Elzero Academy Tooooooooooo Much")) # Tooooooooooo
