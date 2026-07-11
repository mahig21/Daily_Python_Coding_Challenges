#11-07-26
# Given an array of five dice with values 1-6, return the best possible hand.
# 
# Here are the hands ranked lowest to highest:
# 
# Hand                | Description
# --------------------|------------------------------------------
# "no pair"           | No pair or better
# "pair"              | Two dice with the same value
# "two pair"          | Two different pairs
# "three of a kind"   | Three dice with the same value
# "small straight"    | Four consecutive values
# "large straight"    | Five consecutive values
# "full house"        | Three of a kind and a pair
# "four of a kind"    | Four dice with the same value
# "five of a kind"    | All five dice with the same value
def five_dice(dice):
    set_a=set(dice)
    lista=list(set_a)
    if len(set_a)==1:
        return "five of a kind"
    elif len(set_a)==2:
        if dice.count(lista[0])==2 and dice.count(lista[1])==3 or dice.count(lista[0])==3 and dice.count(lista[1])==2:
            return "full house"
        else:
            return "four of a kind"	
    elif len(set_a)==3:
        if dice.count(lista[0])==2 and dice.count(lista[1])==2 or dice.count(lista[0])==2 and dice.count(lista[2])==2 or dice.count(lista[1])==2 and dice.count(lista[2])==2:
            return "two pair"
        else:
            return "three of a kind"
    elif len(set_a)==4:
        return "pair"
    elif len(set_a)==5:
        flag=0
        temp=0
        lista.sort()
        for i in range(0,4):
            if lista[i]+1!=lista[i+1]:
                flag=1
                temp=i
        if flag==0:
            return "large straight"
        else:
            if temp==3:
                return "small straight"
            else:
                return "no pair"

    else:
        return "Invalid range of array"

user_input = input("Enter the values of five dice separated by space: ").split()
dice = [int(num) for num in user_input]
msg=five_dice(dice)
print(msg)