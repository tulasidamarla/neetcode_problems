from collections import Counter


# This approach uses maps. Time complexity is O(s+t), space complexity is O(s+t)
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True


def isAnangramUsingPythonLib(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


# Time complexity is O(s+t).
# This approach may look no extra space but internally sorting algorithms make use of extra space.
def isAnagram2(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def main():
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))
    print(isAnangramUsingPythonLib(s, t))
    s = "car"
    t = "rat"
    print(isAnagram(s, t))
    print(isAnangramUsingPythonLib(s, t))


main()
