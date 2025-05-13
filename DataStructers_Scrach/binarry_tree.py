class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        self.parent = None

class btree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        new_node = Node(val)
        node = self.root

        if self.root == None:
            self.root = new_node
            return 
        
        while new_node.val <= node.val  & node.left != None:
            node = node.left_child
        
        if node.left == None:
            node.left = new_node
            new_node.parent = node
        while new_node.val > node.val and node.right!=None:
            node = node.right
        if node.right == None:
            node.right = new_node
            new_node.parent = node
        

            

        

    def delete(self):
        pass

    def search(self):
        pass

    def _bst(self):
        pass

l = btree()
l.insert(3)
