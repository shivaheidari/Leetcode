"""
head and tail?
size?


"""

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)



class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def __len__(self):
        return self.size
    
    def __iter__(self):
        current = self.head
        while current:
            yield current  # Pause and return current node
            current = current.next

    def __repr__(self):
        nodes = [str(node) for node in self]
        return "->".join(nodes) + "->None"


    

    def print_list(self):
        node = self.head
        while node.next:
            print(node.data)
            node = node.next
        print(node.data)
    
    def is_empty(self):
        return self.size == 0
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def prepend(self, data):
        #add the node at the beggining of the list
        new_node = Node(data)

        if self.is_empty():
            
            self.tail = new_node
        else:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_after(self, target_data, data):
        new_node = Node(data)
        for node in self:
            if node.data == target_data:
                new_node.next = node.next
                node.next = new_node
                if node == self.tail:
                    self.tail = new_node
                self.size += 1
                return 
        raise ValueError(f"Target data {target_data} not found in list")

        
    def delete(self, data):
         """Delete first occurrence of data """

         if self.is_empty():
             return "error"
         
         #general case
         prev = self.head
         for node in self:
             if node.data == data:
                 prev.next = node.next
                 if node == self.tail:
                     self.tail = prev
             self.size -= 1
             prev = node
             
