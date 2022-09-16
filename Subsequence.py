class Solution:
    dict={}
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        index = 0
        for c in t:
            if index == n:
                break
            if c == s[index]:
                index += 1
        return n == index
