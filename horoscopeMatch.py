#12-07-26
"""
    Calculates the compatibility percentage between two star signs.

    The signs are arranged in a circular wheel of 12 positions in this specific order:
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", 
    "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces".
    The sequence wraps back to "Aries" after "Pisces".

    The compatibility is determined by calculating the shortest distance 
    between the two signs on the wheel.

    Distance Mapping:
        0 -> "100%"
        1 -> "40%"
        2 -> "80%"
        3 -> "30%"
        4 -> "90%"
        5 -> "20%"
        6 -> "50%"
    """
signs=["Aries","Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
def compatibilty_match(distance):
    if distance==0:
        return "100%"
    elif distance==1:
        return "40%"
    elif distance==2:
        return "80%"
    elif distance==3:
        return "30%"
    elif distance==4:
        return "90%"
    elif distance==5:
        return "20%"
    elif distance==6:
        return "50%"
    else:
        return compatibilty_match(abs(distance-12))
        

def horoscope_match(sign1, sign2):
    n1=signs.index(sign1)
    n2=signs.index(sign2)
    distance=abs(n1-n2)
    return compatibilty_match(distance)

sign1=input("Enter the first sign: ")
sign2=input("Enter the second sign: ")
compatibilty=horoscope_match(sign1, sign2)
print(compatibilty)