#22-06-26
"""
Given a lowercase string, return it translated into leet speak by replacing 
the letters below with their leet substitutions:

Letter | Leet
-------|------
  a    |  4
  e    |  3
  g    |  9
  i    |  1
  l    |  1
  o    |  0
  s    |  5
  t    |  7

- Characters with no substitution are left unchanged.
"""
def make_leet(s):
    leet_str=""
    leet_dict ={
        'a': '4',
        'e': '3',
        'g': '9',
        'i': '1',
        'l': '1',
        'o': '0',
        's': '5',
        't': '7',
    }
    for i in s:
        if i in leet_dict:
            leet_str+=leet_dict[i]
        else:
            leet_str+=i
    return leet_str
leet_str=make_leet("cool")
print(leet_str)