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
        pass
    
   
    def is_empty(self):
        pass
    def insert_after(self, target_data, data):
        pass
    def delete(self,data):
        pass

l = Double_linked_list()
l.append(3)
l.append(4)
l.append(5)
l.preappend(1)
print(l)