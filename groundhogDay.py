#02-02-26
"""
Today is Groundhog Day, in which a groundhog predicts the weather based
on whether or not it sees its shadow.

Given a value representing the groundhog's appearance, return the
correct prediction:

- If the given value is the boolean True (the groundhog saw its
  shadow), return "Looks like we'll have six more weeks of winter."
- If the value is the boolean False (the groundhog did not see its
  shadow), return "It's going to be an early spring."
- If the value is anything else (the groundhog did not show up), return
  "No prediction this year."
"""
def groundhog_day_prediction(appearance):
    if appearance==True:
        return "Looks like we'll have six more weeks of winter."
    elif appearance==False:
        return "It's going to be an early spring."
    return "No prediction this year."

appearance=input("Did the groundhog see its shadow? (True/False): ")
if appearance=="True":
    appearance=True     
elif appearance=="False":
    appearance=False
prediction=groundhog_day_prediction(appearance)
print(prediction)