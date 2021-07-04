import hangman
import guessing_number

print("Choose your game!")
print("*****************")

print("(1) Hangman, (2) Guessing")
game = int(input("Which game do you wanna play? "))

if game == 1:
    print("So Hangman game it is!")
    hangman.play()
elif game == 2:
    print("So Guessing game it is")
    guessing_number.play()
