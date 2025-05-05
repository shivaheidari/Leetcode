"""
head and tail?

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
            pass
        
    def traverse(self):
        last_node = self.head
        while last_node.next != None:
            last_node = last_node.next
        return last_node

        
    def append(self, data):
        new_node = Node(data)
        insert_point = self.traverse()
        insert_point.next = new_node

    def print_list(self):
        node = self.head
        while node.next:
            print(node.data)
            node = node.next
        print(node.data)
        
    

# l = SinglyLinkedList()
# l.append(1)
# l.append(3)
# l.append(5)
# l.print_list()

def show_status():
    print("Start")
    yield
    print("Middle")
    yield
    print("End")
    yield
status = show_status()
next(status)
next(status)
next(status)

