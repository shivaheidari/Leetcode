class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        reversed=x[::-1]
        return reversed==x


def palindrom (s):
    left = 0 
    right = len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1

        else:
            return False

    return True

print(palindrom("abbac"))