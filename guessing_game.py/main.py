print("Welcome to the Guessing game")
print("****************************")

secret_number = 42
attempts = 3
# turn = 1

# while turn <= attempts:
for turn in range(1, attempts + 1):
    # "R$ {:3.2f}".format() interpolation for: if integer = 3 and float = 2
    # "Sr. {0} {1}.format("Garutti", "Loraine")
    # 3.6 and up: formatted string literals => print(f"My name is {name.lower()}"
    print("\nAttempt {} of {}".format(turn, attempts))
    guess_str = input("type a number between 1 and 100: ")
    print("Your guess was ", guess_str)
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