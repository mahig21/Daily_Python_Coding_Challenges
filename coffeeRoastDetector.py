#22-03-26
"""
Evaluates a string representing coffee beans to determine the roast type.

Bean Point Values:
- Apostrophe (') : 1 point (Light roast bean)
- Dash (-)       : 2 points (Medium roast bean)
- Period (.)     : 3 points (Dark roast bean)

The roast level is determined by the average score of all the beans in the string.

Returns:
    str: 
        - "Light" if the average is less than 1.75.
        - "Medium" if the average is 1.75 to 2.5.
        - "Dark" if the average is greater than 2.5.
"""
def detect_roast(beans):
    points=0
    for i in beans:
        if i=="'":
            points+=1
        elif i=="-":
            points+=2
        elif i==".":
            points+=3
    avg=points/len(beans)
    if avg<1.75:
        return "Light"
    elif avg>=1.75 and avg<=2.5:
        return "Medium"
    elif avg>2.5:
        return "Dark"
beans=input("Enter a string of coffee beans: ")
roast_level=detect_roast(beans)
print(roast_level)