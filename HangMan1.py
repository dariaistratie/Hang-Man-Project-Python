import random
#step 1

word_list =  ["elephant", "giraffe", "kangaroo", "dolphin", "crocodile", "penguin", "octopus"]

word_to_guess=random.choice(word_list)
print(word_to_guess)

guess=input("Guess the letter:").lower()
print(guess)

for letter in word_to_guess:
    if letter == guess:
        print("Right")
else:
        print("Wrong")
