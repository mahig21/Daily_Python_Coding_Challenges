#25-05-26
"""
Given a secret number and a guess, determine if the guess is correct.
Return:
"higher" if the secret number is higher than the guess.
"lower" if the secret number is lower than the guess.
"you got it!" if the guess is correct.
"""
def guess_number(secret, guess):
    if guess==secret:
        return "you got it!"
    elif guess>secret:
        return "lower"
    elif guess<secret:
        return "higher"
secret=int(input("Enter a secret number: "))
guess=int(input("Enter a guess: "))
msg=guess_number(secret, guess)
print(msg)