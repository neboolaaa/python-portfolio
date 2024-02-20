import random
import time
from art import stages, logo
from words import word_list

print(logo)
name =input("\n\nWhat is your name?\n")
time.sleep(0.2)
print(f"\nHello {name}, and Welcome to Hangman!\n\n")

word = random.choice(word_list)
word_length = len(word)
end_of_game = False
lives = 6

time.sleep(0.2)
display = ["_"] * word_length
print(display)

#Testing code
#print(f'Pssst, the solution is {word}.')

while not end_of_game:
    time.sleep(0.2)
    guess = input("Guess a letter: ").lower()
    print("\033c")
    print(f"{logo} \n\n")
    if guess in display:
      print(f"Already guessed {guess}")
    for position in range(word_length):
        letter = word[position]
        if letter == guess:       
            display[position] = letter  
    if guess not in word:
       lives -=1
       print("Incorrect guess. You lose a life")
       if lives == 0:
         end_of_game = True
         print("Sorry! You lose!")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("Congratulations! You win!")
    print(stages[lives])