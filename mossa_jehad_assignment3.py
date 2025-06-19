import random
 
sentence = "Success comes to those who work hard."
print(sentence)

# -1 to make sure that we don't read the null terminator
randomNumber = random.randint(0, len(sentence) - 1)

# +1 because the array of charcters (the string) start from 0 
print("Randomly Selected Index: ", randomNumber + 1)

print("Character at This Index: ", sentence[randomNumber])
