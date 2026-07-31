#22-01-26
"""
    Given an array of exam scores (numbers), return the average score in form of a letter 
    grade according to the following chart:
    
    Average Score | Letter Grade
    -----------------------------
    97-100        | "A+"
    93-96         | "A"
    90-92         | "A-"
    87-89         | "B+"
    83-86         | "B"
    80-82         | "B-"
    77-79         | "C+"
    73-76         | "C"
    70-72         | "C-"
    67-69         | "D+"
    63-66         | "D"
    60-62         | "D-"
    below 60      | "F"
    
    Calculate the average by adding all scores in the array and dividing by the total 
    number of scores.
"""

def get_average_grade(scores):
    avg=sum(scores)//len(scores)
    if avg in range(97,101):
        return "A+"
    elif avg in range(93,97):
        return "A"
    elif avg in range(90,93):
        return "A-"
    elif avg in range(87,90):
        return "B+"
    elif avg in range(83,87):
        return "B"
    elif avg in range(80,83):
        return "B-"
    elif avg in range(77,80):
        return "C+"
    elif avg in range(73,77):
        return "C"
    elif avg in range(70,73):
        return "C-"
    elif avg in range(67,70):
        return "D+"
    elif avg in range(63,67):
        return "D"
    elif avg in range(60,63):
        return "D-"
    elif avg<60:
        return "F"
    else:
        return "Invalid"

scores=input("Enter the scores separated by commas: ")
scores_list=[int(score) for score in scores.split(",")]
print(get_average_grade(scores_list))