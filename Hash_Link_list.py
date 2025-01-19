# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        map_ad={}
        #key is going to be the address and value is the pos
        temp=head
        i=0
        while temp:
            if temp not in map_ad:
                map_ad[temp]=i
                temp=temp.next
                i+=1
            else:
                return True
        return False

            