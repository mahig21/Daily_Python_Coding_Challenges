#24-08-26
"""
Given two strings representing your army and an opposing army, each character from
your army battles the character at the same position from the opposing army using
the following rules:

- Characters a-z have a strength of 1-26, respectively.
- Characters A-Z have a strength of 27-52, respectively.
- Digits 0-9 have a strength of their face value.
- All other characters have a value of zero.
- Each character can only fight one battle.

For each battle, the stronger character wins. The army with more victories, wins the
war. Return the following values:

- "Opponent retreated" if your army has more characters than the opposing army.
- "We retreated" if the opposing army has more characters than yours.
- "We won" if your army won more battles.
- "We lost" if the opposing army won more battles.
- "It was a tie" if both armies won the same number of battles.
"""
def getValue(char):
    if char.isdigit():
        return int(char)
    elif char.isupper():
        return ord(char)-38
    elif char.islower():
        return ord(char)-96
    return 0
def battle(my_army, opposing_army):
    myScore=0
    opponentScore=0
    if len(my_army)>len(opposing_army):
        return "Opponent retreated"
    elif len(my_army)<len(opposing_army):
        return "We retreated"
    for i in range(len(my_army)):
        myArmyVal=getValue(my_army[i])
        oppArmyVal=getValue(opposing_army[i])
        if myArmyVal>oppArmyVal:
            myScore+=1
        elif myArmyVal<oppArmyVal:
            opponentScore+=1
    if myScore==opponentScore:
        return "It was a tie"
    elif myScore>opponentScore:
        return "We won"
    elif myScore<opponentScore:
        return "We lost"

my_army=input("Enter your army: ")
opposing_army=input("Enter the opposing army: ")
print(battle(my_army, opposing_army))