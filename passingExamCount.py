#24-03-26
#Given an array of student exam scores and the score needed to pass it, return the number of students that passed the exam.
def passing_count(scores, passing_score):
    count=0
    for i in scores:
        if i>=passing_score:
            count+=1
    return count
passing_score=int(input("Enter the passing score: "))
scores=[int(x) for x in input("Enter the student scores separated by spaces: ").split()]
count=passing_count(scores, passing_score)
print(count)