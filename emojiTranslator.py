#03-08-26
"""
Given a string of emojis, return the phrase using the following table:

Emoji | Word
------|---------
👶    | "baby"
🐱    | "cat"
🐕    | "dog"
🐟    | "fish"
🥵    | "hot"
🧊    | "ice"
🪨    | "rock"
🦈    | "shark"
🍲    | "soup"
⭐    | "star"

Return the words separated by spaces.
"""
emojis= {
    "👶":	"baby",
    "🐱":	"cat",
    "🐕":	"dog",
    "🐟":	"fish",
    "🥵":	"hot",
    "🧊":	"ice",
    "🪨":	"rock",
    "🦈":	"shark",
    "🍲":	"soup",
    "⭐":	"star"
}
def get_emoji_phrase(s):
    word_list=[]
    for i in s:
        word_list.append(emojis[i])
    return " ".join(word_list)
print(get_emoji_phrase("🧊🧊👶"))