#04-08-26
"""
    Given an array of golf scores and a corresponding array of course par values, return 
    the golfer's handicap index using the following method:

    * Calculate the differential for each round by subtracting the par from the score, 
      then return the average of all differentials rounded to one decimal place.
    """
def calculate_handicap(scores, pars):
    summ=0
    for i in range(len(scores)):
        summ+=scores[i]-pars[i]
    avg=round((summ)/len(scores)+1e-9,1)
    return avg
scores=input("Enter the golf scores separated by spaces: ").split()
pars=input("Enter the course par values separated by spaces: ").split()
scores = [int(x) for x in scores]
pars = [int(x) for x in pars]
print(calculate_handicap(scores, pars))