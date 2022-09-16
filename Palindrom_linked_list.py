# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values=""
        while(head):
            values=values+str(head.val)
            head=head.next
        re=values[::-1]
        return re==values
        