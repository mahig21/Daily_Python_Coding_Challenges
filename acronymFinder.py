#20-04-26
"""
    Given a string representing an acronym, return the full name of the 
    organization it belongs to from the list below:
    
    - "National Avocado Storage Authority"
    - "Cats Infiltration Agency"
    - "Fluffy Beanbag Inspectors"
    - "Department Of Jelly"
    - "Wild Honey Organization"
    - "Eating Pancakes Administration"
    
    Each letter in the given acronym should match the first letter of each word 
    in the organization it belongs to, in the same order.
    """
full_names=["National Avocado Storage Authority",
"Cats Infiltration Agency",
"Fluffy Beanbag Inspectors",
"Department Of Jelly",
"Wild Honey Organization",
"Eating Pancakes Administration"]
def find_org(acronym):
    for i in full_names:
        acro=''
        list_a=i.split()
        for j in list_a:
            acro+=j[0]
        if acronym==acro:
            return i
full_name=find_org("CIA")
print(full_name)