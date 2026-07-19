#27-04-26
"""
Given a word, return its score using a standard letter-value table:

Letter | Value
-------|-------
  A    |   1
  B    |   2
 ...   |  ...
  Z    |  26

* Upper and lowercase letters have the same value.
"""
def get_word_score(word):
    score=0
    for i in word:
        score+=ord(i.upper())-64
    return score
score=get_word_score("hippopotamus")
print(score)