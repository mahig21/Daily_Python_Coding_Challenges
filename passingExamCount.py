#24-03-26
#Given an array of student exam scores and the score needed to pass it, return the number of students that passed the exam.
def passing_count(scores, passing_score):
    count=0
    for i in scores:
        if i>=passing_score:
            count+=1
    return count
count=passing_count([100, 80, 75, 88, 72, 74, 79, 71, 60, 92], 75)
print(count)