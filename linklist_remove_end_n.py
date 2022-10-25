# Definition for singly-linked list.
from html.entities import name2codepoint


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd( head, n):
        #reverse
        #only one node
        if head.next.next==None:
            new_h=head
            
        new_h=reverse_l(head.next.next,head.next)
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


def reverse_l(node,prev):
        if node==None:
            head=prev
            return head
        
        else:
            reverse_l(node,node.next)
            node.next=prev
        

head=ListNode()
n1=ListNode()
n2=ListNode()
n1.val=2
n1.next=n2
n2.val=3
n2.next=None
head.val=None
head.next=n1
removeNthFromEnd(head,1)      
    
