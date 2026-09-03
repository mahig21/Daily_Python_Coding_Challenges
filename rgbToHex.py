#02-09-26
"""
Given a CSS rgb(r, g, b) color string, return its hexadecimal equivalent.

Here are some example outputs for a given input:

Input                 | Output
--------------------- | ---------
"rgb(255, 255, 255)"  | "#ffffff"
"rgb(1, 2, 3)"        | "#010203"

- Make any letters lowercase.
- Return a # followed by six characters. Don't use any shorthand values.
"""
def rgb_to_hex(rgb):
    num=[]
    num_str=""
    hexStr="#"
    for i in rgb:
        if i.isdigit():
            num_str+=i
        else:
            if num_str!="":
                num.append(int(num_str))
            num_str=""
    for i in num:
        hexStr += f"{i:02x}"
    return hexStr
rgb=input("Enter a CSS rgb(r, g, b) color string: ")
print(rgb_to_hex(rgb))

