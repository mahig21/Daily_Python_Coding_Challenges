#04-09-26
"""
Given a string, return a new version of the string where each vowel is duplicated one
more time than the previous vowel you encountered. For instance, the first vowel in
the sentence should remain unchanged. The second vowel should appear twice in a
row. The third vowel should appear three times in a row, and so on.

- The letters 'a', 'e', 'i', 'o', and 'u', in either uppercase or lowercase, are
  considered vowels.
- The original vowel should keep its case.
- Repeated vowels should be lowercase.
- All non-vowel characters should keep their original case.
"""
vowel="aeiouAEIOU"
def repeat_vowels(s):
    repeat=0
    repeatStr=""
    for i in s:
        if i in vowel:
            repeatStr+=i
            for j in range(repeat):
                repeatStr+=i.lower()
            repeat+=1
        else:
            repeatStr+=i
    return repeatStr

s=input("Enter a string: ")
print(repeat_vowels(s))