#08-09-26
"""
Given a string containing one or more words, return an acronym of the words using
the following constraints:

* The acronym should consist of the first letter of each word capitalized, unless
  otherwise noted.
* The acronym should ignore the first letter of these words unless they are the
  first word of the given string: a, for, an, and, by, and of.
* The acronym letters should be returned in the order they are given.
* The acronym should not contain any spaces.
"""
stopwords=['a','for','an','and','by','of']
def build_acronym(s):
    acronym=""
    words=s.split()
    for i in words:
        if i in stopwords and i!=s[0]:
            continue
        acronym+=i[0].upper()
    return acronym
print(build_acronym("Federal Bureau of Investigation"))