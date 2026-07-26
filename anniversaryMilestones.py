#17-03-26
"""
Anniversary Milestones

Given an integer representing the number of years a couple has been married, 
return their most recent anniversary milestone according to this chart:

Years Married | Milestone
--------------|------------
1             | "Paper"
5             | "Wood"
10            | "Tin"
25            | "Silver"
40            | "Ruby"
50            | "Gold"
60            | "Diamond"
70            | "Platinum"

Rules:
- If they haven't reached the first milestone, return "Newlyweds".
"""
milestones = {
    1:"Paper",
    5:"Wood",
    10:"Tin",
    25:"Silver",
    40:"Ruby",
    50:"Gold",
    60:"Diamond",
    70:"Platinum",
}
def get_milestone(years):
    if years==0:
        return "Newlyweds"
    if years in milestones:
        return milestones[years]
    while(years not in milestones):
        years-=1
        if years in milestones:
            return milestones[years]
ans=get_milestone(8)
print(ans)