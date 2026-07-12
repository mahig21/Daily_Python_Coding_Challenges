#29-06-26
# Given a genre string and a BPM number for a song, determine the mood using the following table:
#
# | Mood    | Genre        | BPM Range |
# |---------|--------------|-----------|
# | "focus" | "classical"  | 60-109    |
# | "focus" | "electronic" | 60-89     |
# | "happy" | "pop"        | 60-180    |
# | "happy" | "classical"  | 110-180   |
# | "happy" | "rock"       | 60-129    |
# | "happy" | "electronic" | 90-134    |
# | "hype"  | "rock"       | 130-180   |
# | "hype"  | "electronic" | 135-180   |

def get_mood(genre, bpm):
    if genre=="classical" and (bpm>=60 and bpm<=109):
        return "focus"
    elif genre=="electronic" and (bpm>=60 and bpm<=89):
        return "focus"
    elif genre=="pop" and (bpm>=60 and bpm<=180):
        return "happy"
    elif genre=="classical" and (bpm>=110 and bpm<=180):
        return "happy"
    elif genre=="rock" and (bpm>=60 and bpm<=129):
        return "happy"
    elif genre=="electronic" and (bpm>=90 and bpm<=134):
        return "happy"
    elif genre=="rock" and (bpm>=130 and bpm<=180):
        return "hype"
    elif genre=="electronic" and (bpm>=135 and bpm<=180):
        return "hype"
mood=get_mood("classical", 180)
print(mood)