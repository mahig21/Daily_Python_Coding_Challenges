#11-05-26
"""
    Given an array of objects, each with a "name" and "age" property, return
    an array containing the name of the oldest person.
    
    If multiple people share the oldest age, return all of their names in the order
    they appear in the input.
"""
def get_oldest(people):
    oldest=[]
    maxAge=0
    for i in people:
        if i['age']>maxAge:
            maxAge=i['age']
    for i in people:
        if i['age']==maxAge:
            oldest+=[i['name']]
    return oldest
oldest=get_oldest([{ "name": "Allison", "age": 25 }, { "name": "Bill", "age": 30 }, { "name": "Carol", "age": 30 }])
print(oldest)