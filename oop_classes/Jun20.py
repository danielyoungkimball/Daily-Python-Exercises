from typing import List

def group_anagrams(words: List[str]) -> List[List[str]]:
    groups = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())

# Example usage
if __name__ == "__main__":
    words = ["bat", "tab", "tap", "pat", "cat"]
    result = group_anagrams(words)
    print(result)
