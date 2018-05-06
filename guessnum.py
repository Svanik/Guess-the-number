import random


def takeguess():
    global guess
    guess = input("Take a Guess:")
    valguess()


def valguess():
    global guess
    if guess.isnumeric():
        guess = int(guess)
    else:
        print("Your guess was not a number")
        takeguess()
        return True


def testguess():
    global guess
    global target

    if guess > target:
        highguess()
    elif guess < target:
        lowguess()
    else:
        return 1


def highguess():
    print("Your Guess was too high try again")


def lowguess():
    print("Your Guess was too low try again")


target = random.randint(1, 100)
guess = -1
count = 0

print("Guess the Number it is between 1 and 100")
while (guess != target):
    takeguess()
    count += 1
    if testguess() == 1:
        break


print(f"Congratulations You Guessed Correctly it took you {count} guesses")
