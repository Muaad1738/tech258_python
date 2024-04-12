from random import randint

print("Welcome to dice game")

print("Let's play dice game, are you ready")
ready = input()

print("Name please")
name = input()

while True:
    user_roll = randint(1, 6)
    comp_roll = randint(1, 6)

    print("You rolled:", user_roll)
    print("Computer rolled:", comp_roll)

    if user_roll > comp_roll:
        print("You win!")
    else:
        print("You lose!")
