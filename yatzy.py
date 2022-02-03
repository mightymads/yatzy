import random


def check_roll(rolled_dice):

    valid_score = {
        'pair of ones': [1, 1],
        'pair of twos': [2, 2],
        'pair of threes': [3, 3],
        'pair of fours': [4, 4],
        'pair of fives': [5, 5],
        'pair of sixes': [6, 6],
        'two pair of ones and twos': [2, 2, 1, 1],
        'two pair of ones and threes': [3, 3, 1, 1],
        'two pair of ones and fours': [4, 4, 1, 1],
        'two pair of ones and fives': [5, 5, 1, 1],
        'two pair of ones and sixes': [6, 6, 1, 1],
        'two pair of twos and threes': [3, 3, 2, 2],
        'two pair of twos and fours': [4, 4, 2, 2],
        'two pair of twos and fives': [5, 5, 2, 2],
        'two pair of twos and sixes': [6, 6, 2, 2],
        'two pair of threes and fours': [4, 4, 3, 3],
        'two pair of threes and fives': [5, 5, 3, 3],
        'two pair of threes and sixes': [6, 6, 3, 3],
        'two pair of fours and fives': [5, 5, 4, 4],
        'two pair of fours and sixes': [6, 6, 4, 4],
        'two pair of fives and sixes': [6, 6, 5, 5],
        'three of a kind in ones': [1, 1, 1],
        'three of a kind in twos': [2, 2, 2],
        'three of a kind in threes': [3, 3, 3],
        'three of a kind in fours': [4, 4, 4],
        'three of a kind in fives': [5, 5, 5],
        'three of a kind in sixes': [6, 6, 6],
        'four of a kind in ones': [1, 1, 1, 1],
        'four of a kind in twos': [2, 2, 2, 2],
        'four of a kind in threes': [3, 3, 3, 3],
        'four of a kind in fours': [4, 4, 4, 4],
        'four of a kind in fives': [5, 5, 5, 5],
        'four of a kind in sixes': [6, 6, 6, 6],
        'small straight': [1, 2, 3, 4, 5],
        'big straight': [2, 3, 4, 5, 6],
        'full house of ones and twos': [2, 2, 1, 1, 1],
        'full house of ones and threes': [3, 3, 1, 1, 1],
        'full house of ones and fours': [4, 4, 1, 1, 1],
        'full house of ones and fives': [5, 5, 1, 1, 1],
        'full house of ones and sixes': [6, 6, 1, 1, 1],
        'full house of twos and ones': [2, 2, 2, 1, 1],
        'full house of twos and threes': [3, 3, 2, 2, 2],
        'full house of twos and fours': [4, 4, 2, 2, 2],
        'full house of twos and fives': [5, 5, 2, 2, 2],
        'full house of twos and sixes': [6, 6, 2, 2, 2],
        'full house of threes and twos': [3, 3, 3, 2, 2],
        'full house of threes and fours': [4, 4, 3, 3, 3],
        'full house of threes and fives': [5, 5, 3, 3, 3],
        'full house of threes and sixes': [6, 6, 3, 3, 3],
        'full house of fours and ones': [4, 4, 4, 1, 1],
        'full house of fours and twos': [4, 4, 4, 2, 2],
        'full house of fours and threes': [4, 4, 4, 3, 3],
        'full house of fours and fives': [4, 4, 4, 5, 5],
        'full house of fours and sixes': [4, 4, 4, 6, 6],
        'full house of fives and ones': [5, 5, 5, 1, 1],
        'full house of fives and twos': [5, 5, 5, 2, 2],
        'full house of fives and threes': [5, 5, 5, 3, 3],
        'full house of fives and fours': [5, 5, 5, 4, 4],
        'full house of fives and sixes': [5, 5, 5, 6, 6],
        'full house of sixes and ones': [6, 6, 6, 1, 1],
        'full house of sixes and twos': [6, 6, 6, 2, 2],
        'full house of sixes and threes': [6, 6, 6, 3, 3],
        'full house of sixes and fours': [6, 6, 6, 4, 4],
        'full house of sixes and fives': [6, 6, 6, 5, 5],
        'yatzy of sixes': [6, 6, 6, 6, 6],
        'yatzy of fives': [5, 5, 5, 5, 5],
        'yatzy of fours': [4, 4, 4, 4, 4],
        'yatzy of threes': [3, 3, 3, 3, 3],
        'yatzy of twos': [2, 2, 2, 2, 2],
        'yatzy of ones': [1, 1, 1, 1, 1]
    }

    # TODO: Handle Chance and regular 1-6

    rolled_dice.sort(reverse=True)
    org_rolled_dice = rolled_dice.copy()
    comparison_result = []
    text_results = []
    for key, value in valid_score.items():
        rolled_dice = org_rolled_dice.copy()
        length = len(value)
        i = 0
        while i < length:
            x = 0
            while x < len(rolled_dice):
                if value[i] == rolled_dice[x]:
                    comparison_result.append(rolled_dice[x])
                    rolled_dice.pop(x)
                    break
                x += 1
            i += 1

        if value == comparison_result:
            print(key)
            text_results.append(key)

        comparison_result = []
    print("ROLLED DICE: " + str(org_rolled_dice))
    print("TEXT RESULT: " + str(text_results))
    return(text_results)


"""
# TODO: Do we really need dies to be class based?
class Die:
    # A regular die which can be rolled
    # When rolled it returns a value between 1 and 6

    def __init__(self):
        random.seed()

        # set initial face value
        self.face_value = 0
        self.roll()

    def get_face_value(self):
        return self.face_value

    def roll(self):
        self.face_value = random.randrange(1, 7)
        return self.face_value
"""


def roll_dice(dice):
    rolled_dice = []
    for die in dice:
        die = random.randrange(1, 7)
        rolled_dice.append(die)
        rolled_dice.sort(reverse=True)
    return rolled_dice
    #return [6, 5, 3, 3, 1]


def setup_game():
    dice = [1, 2, 3, 4, 5]
    return dice


def play_round(dice):
    # here we allow the player to roll three times
    # the user can 'hold' one or more dies and roll the remaining dice
    roll_count = 1
    held_dice = []
    do_roll = False
    do_check = False
    dice_held = False
    while roll_count <= 3:
        if roll_count == 1:
            print("Let's play")
            print("You have three rolls to get a result")
            input("Hit Enter to roll dice")
            do_roll = True
            do_check = True

        else:
            print("Enter the face value of each die you want to hold e.g '6 6' to hold a pair of sixes. "
                  "Enter 'all' to roll all dice. "
                  "Enter 'stop' to stop your round.")

            actions = input().split(" ")

            if 'all' in actions:
                do_roll = True
                do_check = True
                #dice_held = False
            elif 'stop' in actions:
                do_roll = False
                do_check = True
                #dice_held = False
                roll_count = 100  # soft break
            else:
                # convert list elements to integers
                actions = [int(action) for action in actions]
                actions.sort(reverse=True)
                print(actions)

                for action in actions:
                    if action in [1, 2, 3, 4, 5, 6]:
                        held_dice.append(action)
                        dice.remove(action)
                        #dice_held = True
                    else:
                        # invalid input, just repeat the loop
                        do_roll = False
                        do_check = False
                        #dice_held = False

                if len(held_dice) > 0:
                    dice_held = True
                    print("Holding: " + str(held_dice))
                else:
                    dice_held = False

        if do_roll:
            dice = roll_dice(dice)
            roll_count += 1
            print("You rolled: " + str(dice))
            print()

        if do_check:
            if dice_held:
                dice += held_dice
                held_dice = []
            check_roll(dice)

    #for action in actions:
    print(held_dice)
    print(dice)
    #roll_dice(reroll_dice)
    #check_roll(dice)


def show_banner():
    print("#" * 50)
    print("#" + " " * 48 + "#")
    print("#" + " " * 16 + "MIGHTYMADS YATZY" + " " * 16 + "#")
    print("#" + " " * 48 + "#")
    print("#" * 50)


#
# MAIN
#

show_banner()
play_round(setup_game())


"""
    for key, value in valid_score.items():
        length = len(value)
        i = 0
        while i < length:
            if value[i] == rolled_dice[i]:
                comparison_result.append(rolled_dice[i])
            else:
                zero_fillers.append(0)
            i += 1
        comparison_result += zero_fillers
        if value == comparison_result:
            print(key)
        print(comparison_result)
        comparison_result = []
        zero_fillers = []
"""







