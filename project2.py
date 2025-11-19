import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    sum = die1 + die2
    print(f"The sum of dice is: {die1} + {die2} = {sum}")
    return sum

def play_craps():
    first_roll = roll_dice()

    if first_roll == 7 or first_roll == 11:
        print("You won!")
        return
    elif first_roll == 2 or first_roll == 3 or first_roll == 12:
        print("The casino wins!")
        return
    else:
        goal = first_roll
        print(f"Your goal number is: {goal}")
    
    while True:
        roll = roll_dice()
        if roll == goal:
            print("You won!")
            break
        elif roll == 7:
            print("You lose!")
            break

play_craps()
