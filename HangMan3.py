import random  # importam cuvinte random

#step3
# List of words to choose from

word_list =  ["elephant", "giraffe", "kangaroo", "dolphin", "crocodile", "penguin", "octopus"]
# Function to select a random word from the list

word_to_guess = random.choice(word_list)
print(word_to_guess)

placeholder = ""
word_length = len(word_to_guess)
for position in range(word_length):
    placeholder += "_"
print(placeholder)


# Folosim bucla while loop
game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in word_to_guess:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You win.")

