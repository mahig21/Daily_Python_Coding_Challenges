#26-02-26
"""
Letter and Number Count

Given a string, returns a message with the count of how many letters and 
numbers it contains.

Rules:
- Letters are A-Z and a-z.
- Numbers are 0-9.
- Ignores all other characters.

Returns:
A string formatted as "The string has X letters and Y numbers." 
Dynamically uses the singular form ("letter" or "number") if the respective 
count is exactly 1.
"""
def count_letters_and_numbers(s):
    letters = 0
    digits = 0
    for i in s:
        if i.isalpha():
            letters += 1
        elif i.isdigit():
            digits += 1
    letter_word = "letter" if letters == 1 else "letters"
    number_word = "number" if digits == 1 else "numbers"
    return f"The string has {letters} {letter_word} and {digits} {number_word}."

output_str = count_letters_and_numbers("A1!")
print(output_str)