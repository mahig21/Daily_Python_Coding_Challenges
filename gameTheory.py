#23-07-26
"""
Given two equal length strings representing two players' strategies for a game, 
return the scores as an array [player1, player2].

* The given strings will only contain one of two letters: "C" (cooperate) or "D" (defect).
* Each character represents one round, scored as follows:
    - If both players cooperate, each scores 3.
    - If both players defect, each scores 1.
    - If one player defects and the other cooperates, the defector scores 5 and the cooperator scores 0.
"""
def play_game(p1, p2):
    p1_score=0
    p2_score=0
    score=[]
    for i in range(len(p1)):
        if p1[i]=='C' and p2[i]=='C':
            p1_score+=3
            p2_score+=3
        elif p1[i]=='D' and p2[i]=='D':
            p1_score+=1
            p2_score+=1
        elif p1[i]=='D' and p2[i]=='C':
            p1_score+=5
        elif p1[i]=='C' and p2[i]=='D':
            p2_score+=5
    score.append(p1_score)
    score.append(p2_score)
    return score
score=play_game("CCCDCDCCCDDC", "CCDDCDCDDCCD")
print(score)