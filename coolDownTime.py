#25-03-26
"""
Exam Retake Eligibility

Given two timestamps, the first representing when a user finished an exam,
and the second representing the current time, determine whether the user
can take an exam again.

Rules:
- Both timestamps will be given the format: "YYYY-MM-DDTHH:MM:SS",
  for example "2026-03-25T14:00:00". Note that the time is 24-hour clock.
- A user must wait at least 48 hours before retaking an exam.
"""
import datetime
def can_retake(finish_time, current_time):
    finish=datetime.datetime.strptime(finish_time,"%Y-%m-%dT%H:%M:%S")
    current=datetime.datetime.strptime(current_time,"%Y-%m-%dT%H:%M:%S")
    delta=datetime.timedelta(days=2)
    if current-finish>=delta:
        return True
    return False

ans=can_retake("2026-03-23T08:00:00", "2026-03-25T14:00:00")
print(ans)