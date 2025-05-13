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
        if node == None:
            self.root = new_node
            print("inserted", new_node.val)
            return

        while node!=None:
            if node.val >= new_node.val:
                if node.left == None:
                    node.left = new_node
                    new_node.parent = node
                    return
                else:
                 node = node.left 
            if node.val < new_node.val:
                if node.right == None:
                    node.right = new_node
                    new_node.parent = node
                    return
                else:
                    node = node.right
            

    def delete(self):
        pass

    def search(self):
        pass

    def _bst(self):
        pass
    
    def print_tree(self):
        self._travers_inorder(self.root)

    def _travers_inorder(self, node):
            
        if node != None:
            
            self._travers_inorder(node.left)
            print(node.val)
            self._travers_inorder(node.right)
        return
            

    def _travers_postorder(self, node):      
        pass
    def _travers_preorder(self, node):
        pass
    def _travers_levelorder(self, node):
        pass
l = btree() 
l.insert(10)
l.insert(5)
l.insert(3)
l.insert(7)
l.insert(20)
l.insert(15)
l.insert(16)
l.insert
l.print_tree()


