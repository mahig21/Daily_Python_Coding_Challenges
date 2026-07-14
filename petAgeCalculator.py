#14-07-26
"""
Given a pet type and age in human years, return the equivalent age in pet 
years using the following conversion table:

| Pet          | Multiplier |
|--------------|------------|
| "dog"        | 7          |
| "cat"        | 6          |
| "rabbit"     | 8          |
| "hamster"    | 30         |
| "guinea pig" | 12         |
| "goldfish"   | 6          |
| "bird"       | 5          |
"""
def pet_years(pet, age):
    age_dict = {
        "dog": 7,
        "cat": 6,
        "rabbit": 8,
        "hamster": 30,
        "guinea pig": 12,
        "goldfish": 6,
        "bird": 5
    }
    return age*age_dict[pet]
    
petYears=pet_years("hamster", 4)
print(petYears)