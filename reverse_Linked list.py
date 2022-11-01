#iterative solution 
def reverse_l(head):
       prev, curr=None,head
       while curr:
        temp=curr.next
        curr.next=prev
        prev=curr
        curr=temp
       return prev 
       
def revese_rec(head):
    if not head:
        return None
    newhead=head
    if head.next:
        newhead=revese_rec(head.next)
        head.next.next=head
    return newhead
        
