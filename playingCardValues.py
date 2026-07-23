#04-03-26
"""
Given an array of playing cards, return a new array with the numeric value of each card.

Card Values:
- An Ace ("A") has a value of 1.
- Numbered cards ("2" - "10") have their face value: 2 - 10, respectively.
- Face cards: Jack ("J"), Queen ("Q"), and King ("K") are each worth 10.

Suits:
- Each card has a suit: Spades ("S"), Clubs ("C"), Diamonds ("D"), or Hearts ("H").

Card Format:
- Each card is represented as a string: "valueSuit". For Example: "AS" is the 
  Ace of Spades, "10H" is the Ten of Hearts, and "QC" is the Queen of Clubs.
"""
card_value = {
    'A':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    'J':10,
    'Q':10,
    'K':10,

}
def card_values(cards):
    values=[]
    for i in cards:
        values.append(card_value[i[:-1]])
    return values
cards=input("Enter list of cards separated by commas: ").split(",")
values=card_values(cards)
print(values)