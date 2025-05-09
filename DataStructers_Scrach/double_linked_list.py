class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    def __repr__(self):
        return str(self.data)
    

class Double_linked_list:
    def __init__(self):
        
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next


    def __repr__(self):
        nodes = [str(node)for node in self]
        return "->".join(nodes)+"->None"
    
    def append(self, data):
        #insert at the end
        node = Node(data)
        if self.size == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node

        self.size += 1


    def head_tail(self):
        return self.head, self.tail 
     
    def search(self, data):
        #return true if data is in the list
        for node in self:
            if node.data == data:
                return True
        return False

    def preappend(self, data):
        #insert at the begining
        node = Node(data)
        self.head.prev = node
        node.next = self.head
        self.head = node

        
    def reverse(self):
        node = self.head
        while node!= None:
            target = node.next
            node.next, node.prev = node.prev, node.next
            node = target

        self.head, self.tail = self.tail, self.head
   
    def is_empty(self):
        return self.size == 0
    
    def insert_after(self, target_data, data):
        pass

    def delete(self,data):
        node = self.head
        while node != None:
            if node.data == data:
                if node == self.head:
                    node.next.prev = None
                    self.head = node.next
                    self.size -= 1
                elif node == self.tail:
                    node.prev.next = None
                    self.tail = node.prev
                    self.size -= 1

                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    self.size -= 1
            node = node.next

l = Double_linked_list()
l.append(3)
l.append(4)
l.append(5)
print(l)
l.reverse()
l.append(1)
l.preappend(0)
print(l)
l.delete(1)
print(l)