#04-02-26
#Given a string, return it as-is if it's 20 characters or shorter. If it's longer than 20 characters, truncate it to the first 17 characters and append "..." to the end of it (so it's 20 characters total) and return the result.
def truncate_text(text):
    lenn=len(text)
    if lenn<=20:
        return text
    else:
        return text[:17]+"..."
text=input("Enter a string: ")
print(truncate_text(text))