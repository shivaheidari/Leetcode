class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        reversed=x[::-1]
        return reversed==x