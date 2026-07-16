#16-07-25
"""
    Given a string, convert it to Pig Latin using the following rules:
    
    * If a word begins with a vowel ("a", "e", "i", "o", or "u"), add 
      "way" to the end. For example, "universe" converts to "universeway".
    * If a word begins with one or more consonants, move them to the end 
      and add "ay". For example, "hello" converts to "ellohay".
    * Preserve the case of the first letter. For example, "Hello" converts 
      to "Ellohay".
    """
def pig_latin(s):
    ans=""
    word_list=s.split()
    for i in word_list:
        con=""
        if word_list.index(i)!=0:
            ans+=" "
        if i[0].isalpha():
            if i[0].lower() in "aeiou":
                ans+=i+"way"
            else:
                for j in i:
                    if j not in "aeiou":
                        con+=j
                    else:
                        break
                len1=len(con)
                if i[0].isupper():
                    ans+=i[len1].upper()+i[len1+1:]+con.lower()+"ay"
                else:
                    ans+=i[len1:]+con+"ay"
    return ans
ans=pig_latin("The quick brown fox jumped over the lazy dog") 
print(ans)