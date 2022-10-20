# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        htemp=head_heap=ListNode()
        resutl=[]  
        for k in range(0, len(lists)):
            ltemp=head_list=lists[k]
            # if head_heap.next=null:
            #     head_heap=ltemp
            if htemp.val >= ltemp.val:
                #Goes to the left side
                #finding insertion point
                inspoint=head_heap
                while(inspoint.val<ltemp.val):
                    inspoint=inspoint.next
                ltemp.next=inspoint.next
                inspoint.next=ltemp
            else:
                #go to the right side
                #finding the insertion point
                inspoint=htemp.next
                while(inspoint.val < ltemp.val):
                    inspoint=inspoint.next
                ltemp.next=inspoint.next
                inspoint.next=ltemp
            ltemp=ltemp.next 
         
            while(head_heap):
                result.append(head_heap.val)
                head_heap=head_heap.next
            return result  
            


    


    
        #make a heap 
        # for k in list of list and each element check the heap