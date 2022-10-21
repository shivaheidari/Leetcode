# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        map_nodes={}
        temp=head
        i=0
        while temp:
            if temp.next not in map_nodes:
                map_nodes[temp]=i
                temp=temp.next
                i+=1
            else:
                return temp.next
        return None