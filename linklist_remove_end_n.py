# Definition for singly-linked list.
from html.entities import name2codepoint
from urllib.request import HTTPDigestAuthHandler


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
        #reverse
        #only one node
        if head.next.next==None:
            new_h=head
            
        new_h=reverse_l(head.next)
        #delete
        i=0
        temp=new_h
        prev=None
        while(temp):
            i+=1
            if n==1:
                new_h=new_h.next
            
            
            elif(i != n):
                prev=temp
                
            else:
                prev.next=temp.next
            temp=temp.next

        #reverse
        head=reverse_l(new_h)
        return head


def reverse_l(head):
    if not head:
        return None
    newhead=head
    if head.next:
        newhead=reverse_l(head.next)
        head.next.next=head
        head.next=None
    return newhead
       
        
def print_l(head):
    while(head):
        print(head.val)
        head=head.next


head=ListNode()
n1=ListNode()
n2=ListNode()
n3=ListNode()
n1.val=2
n1.next=n2
n2.val=3
n2.next=n3
n3.val=4
n3.next=None
head=n1
print_l(head)
head=removeNthFromEnd(head,1)
# head=reverse_l(head)
print_l(head)

# removeNthFromEnd(head,1)      
    
