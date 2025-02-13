import random
#step4
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list =  ["elephant", "giraffe", "kangaroo", "dolphin", "crocodile", "penguin", "octopus"]
lives=6


word_to_guess = random.choice(word_list)
print(word_to_guess)

placeholder = ""
word_length = len(word_to_guess)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

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



    if guess not in word_to_guess:
        lives -=1
    if lives == 0:
        game_over = True
        print("You lose!")

    if "_" not in display:
        game_over = True
        print("You win.")



print(stages[lives])