import random
#step2
word_list =  ["elephant", "giraffe", "kangaroo", "dolphin", "crocodile", "penguin", "octopus"]

chosen_word = random.choice(word_list)
print(chosen_word)



placeholder=" "
word_length=len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)


guess = input("Guess a letter: ").lower()


display=" "
for letter in chosen_word:
    if letter == guess:
      display += letter
    else:
       display +=" "