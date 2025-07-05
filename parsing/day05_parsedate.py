# 🐍 Python Daily Challenge: Longest Streak

# You’re given a list of dates (as strings in "YYYY-MM-DD" format), representing the days
# a user logged into a system. The list may be unordered and may contain duplicates.

# dates = [
#     "2025-07-01",
#     "2025-07-03",
#     "2025-07-02",
#     "2025-07-02",
#     "2025-06-30",
#     "2025-07-05",
#     "2025-07-06",
# ]

# longest_streak(dates) ➞ 4
# Streak: 2025-06-30 → 2025-07-03


from typing import List
from datetime import datetime, timedelta


def longest_streak(dates: List[str]) -> int:
    if not dates:
        return 0

    # Convert to date objects & remove duplicates
    date_objs = sorted(set(datetime.strptime(d, "%Y-%m-%d").date() for d in dates))

    longest = 1
    current = 1

    for i in range(1, len(date_objs)):
        if date_objs[i] == date_objs[i - 1] + timedelta(days=1):
            current += 1
            longest = max(longest, current)
        else:
            current = 1

    return longest


if __name__ == "__main__":
    dates = [
        "2025-07-01",
        "2025-07-03",
        "2025-07-02",
        "2025-07-02",
        "2025-06-30",
        "2025-07-05",
        "2025-07-06",
    ]
    assert longest_streak(dates) == 4
    print("Successfully passed all tests")
