#08/07/26
# Given a number of milliseconds since the last post on an issue, 
# and the last message posted on the issue, determine what you 
# should do with the issue according to these rules:
# - If the last message is less than 7 days ago, return "leave it"
# - If the last message is 7 or more days ago and its content 
#   contains "bump" (case-insensitive), return "close it"
# - Otherwise, return "bump it"
def triage_issue(ms, message):
    if (ms<86400000*7):
        return "leave it"
    elif (ms>=86400000*7 and "bump" in message.lower()):
        return "close it"
    else:
        return "bump it"
msg=triage_issue(604800000, "Bumping this")
print(msg)