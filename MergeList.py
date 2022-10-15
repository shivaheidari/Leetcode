# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result=head=ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                head.next=list1
                head=head.next
                list1=list1.next
            else:
                head.next=list2
                head=head.next
                list2=list2.next
        if list1 or list2:
            head.next=list1 if list1 else list2 
        return result.next