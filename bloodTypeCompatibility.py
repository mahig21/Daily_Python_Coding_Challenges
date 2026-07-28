#23-02-26
"""
Blood Type Compatibility

Given a donor blood type and a recipient blood type, determine whether
the donor can give blood to the recipient.

Each blood type consists of:
- A letter: "A", "B", "AB", or "O"
- And an Rh factor: "+" or "-"

Blood types will be one of the valid letters followed by an Rh factor. For
example, "AB+" and "O-" are valid blood types.

Letter Rules:
- "O" can donate to other letter type.
- "A" can donate to "A" and "AB".
- "B" can donate to "B" and "AB".
- "AB" can donate only to "AB".

Rh Rules:
- Negative ("-") can donate to both "-" and "+".
- Positive ("+") can donate only to "+".

Both letter and Rh rule must pass for a donor to be able to donate to the
recipient.
"""
def can_donate(donor, recipient):
    donor_sign=donor[-1]
    donorBG=donor[:-1]
    recipient_sign=recipient[-1]
    recipientBG=recipient[:-1]
    if donor_sign=='+' and recipient_sign=='-':
        return False
    elif donorBG=='O' or recipientBG=='AB':
        return True
    elif donorBG==recipientBG:
        return True
    return False
ans=can_donate("A+", "AB+")
print(ans)