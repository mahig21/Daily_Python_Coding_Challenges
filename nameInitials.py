#13-04-26
"""
Given a full name as a string, return their initials.

- Names to initialize are separated by a space.
- Initials should be made uppercase.
- Initials should be separated by dots.
"""
def get_initials(name):
    name=name.split()
    initials=""
    for i in name:
        initials+=i[0]+"."
    return initials
initials=get_initials("Savanna Puddlesplash")
print(initials)