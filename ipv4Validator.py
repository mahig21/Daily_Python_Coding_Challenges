#05-09-26
"""
Given a string, determine if it is a valid IPv4 Address. A valid IPv4 address consists of
four integer numbers separated by dots (.). Each number must satisfy the following
conditions:

- It is between 0 and 255 inclusive.
- It does not have leading zeros (e.g. 0 is allowed, 01 is not).
- Only numeric characters are allowed.
"""
def is_valid_ipv4(ipv4):
    if ipv4.count(".")!=3:
        return False
    classes=ipv4.split(".")
    for i in classes:
        if len(classes)!=4 or i=="":
            return False
        for j in i:
            if not j.isdigit():
                return False
        if int(i)>255 or int(i)<0:
            return False
        if (i[0]=='0' and int(i)!=0) or (i.count('0')>1 and int(i)==0):
            return False
    return True
print(is_valid_ipv4("255.01.50.111"))
print(is_valid_ipv4("192168145213"))
print(is_valid_ipv4("256.101.50.115"))
print(is_valid_ipv4("192.168.1.1"))