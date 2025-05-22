from random import randint

def roll(number_of_dice, dice_type=6, score_modifier=0):
    dice_allowed = list((3, 4, 6, 8, 10, 12, 100))
    if dice_type not in dice_allowed:
        raise Exception("No such dice")
    result = 0
    for _ in range(number_of_dice):
        result += randint(1, dice_type)
    result += score_modifier
    return result

print(roll(2, 10, 20))  # Rolls two 10-sided dice and adds 20
print(roll(3, 6, -3))   # Rolls three 6-sided dice and subtracts 3
