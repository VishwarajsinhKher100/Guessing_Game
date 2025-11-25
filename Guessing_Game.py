import random

correct_num = random.randint(1, 100)
guess_num = int(input("Guess the number: "))
counter = 1

while guess_num != correct_num:
    if guess_num < correct_num:
        print("Guess higher")
    else:
        print("Guess lower")

    guess_num = int(input("Guess the number: "))
    counter += 1

print(f"Correct guess, you took {counter} attempts")