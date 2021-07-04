import random


def play():
    print("Welcome to Guessing game")
    print("************************")

    secret_number = random.randrange(1, 101)
    attempts = 0
    points = 1000
    # turn = 1

    print("Choose a difficulty level: ")
    print("(1) Easy, (2) Normal, (3) Hard")

    level = int(input("Type a number: "))

    if level == 1:
        attempts = 20
    elif level == 2:
        attempts = 10
    else:
        attempts = 5

    # while turn <= attempts:
    for turn in range(1, attempts + 1):
        # "R$ {:3.2f}".format() interpolation for: if integer = 3 and float = 2
        # "Sr. {0} {1}.format("Garutti", "Loraine")
        # 3.6 and up: formatted string literals => print(f"My name is {name.lower()}"
        print("\nAttempt {} of {}".format(turn, attempts))
        guess_str = input("Type a number between 1 and 100: ")
        guess = int(guess_str)

        if guess < 1 or guess > 100:
            print("Please, type a number between 1 and 100")
            continue

        won = guess == secret_number
        higher = guess > secret_number
        smaller = guess < secret_number

        if won:
            print("You won!")
            break
        else:
            if higher:
                print("You missed, your number is higher than the expected number")
            elif smaller:
                print("You missed, your number is smaller than the expected number")

        # turn = turn + 1

    print("\nEnd game")


if __name__ == "__main__":
    play()
