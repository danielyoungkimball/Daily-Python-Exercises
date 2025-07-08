# 🐍 Python Exercise: Detect the First Non-Repeating Character

# INSTRUCTIONS:
# Write a function called `first_unique_char` that takes a string input
# and returns the **first character** that does not repeat anywhere in the string.
# If all characters repeat, return `None`.

# EXAMPLE INPUTS / OUTPUTS:
# first_unique_char("swiss") => "w"
# first_unique_char("redivider") => "v"
# first_unique_char("aabbcc") => None

# HINT:
# - You might want to use a dictionary to count characters.
# - Then loop again to find the first with count == 1.


def first_unique_char(s: str) -> str | None:
    freq = {}
    for char in s:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1

    for char in s:
        if freq[char] == 1:
            return char

    return None


from collections import Counter


def first_unique_char_opt(s: str) -> str | None:
    freq = Counter(s)
    return next((char for char in s if freq[char] == 1), None)


# ✅ TEST CASES:
# print(first_unique_char("swiss"))  # should return "w"
# print(first_unique_char("redivider"))  # should return "v"
# print(first_unique_char("aabbcc"))  # should return None
# print(first_unique_char("racecar"))  # should return "e"
# print(first_unique_char(""))  # should return None

# 🧠 BONUS CHALLENGE:
# Make the function **case-insensitive** without changing the original input.
# So `first_unique_char("Swiss")` should still return "w"

# if __name__ == "__main__":
#     assert first_unique_char("swiss") == "w"
#     assert first_unique_char("redivider") == "v"
#     print("Successfully passed all tests!")

# 🐍 Python Exercise: First Non-Repeating Word

# INSTRUCTIONS:
# Write a function `first_unique_word(sentence: str) -> str | None`
# that returns the first **word** in the sentence that appears only once.
# If all words repeat, return `None`.

# Words are case-insensitive but the original casing should be returned.
# Assume words are separated by spaces and contain only letters.

# EXAMPLE:
# first_unique_word("The cat chased the cat") => "chased"
# first_unique_word("Hello hello world") => "world"
# first_unique_word("one one one") => None

# HINT:
# - Split the sentence into words.
# - Use a dictionary or Counter to track frequency.
# - Make comparison case-insensitive, but return original word.

def first_unique_word(sentence: str):
    # Split sentence into words
    words = sentence.split()
    lower_words = [word.lower() for word in words]

    freq = Counter(lower_words)

    for i, word in enumerate(words):
        if freq[lower_words[i]] == 1:
            return word
    
    return None

if __name__ == "__main__":
    assert first_unique_word("The cat chased the cat") == "chased"
    assert first_unique_word("Hello hello world") == "world"
    assert first_unique_word("one one one") == None
    print("Successfully passed all tests!")