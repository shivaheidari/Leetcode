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
        if self.root is None:
            self.root = new_node
            return
        node = self.root

        while True:
            if val < node.val:
                if node.left is None:
                    node.left = new_node
                    new_node.parent = node
                    return
                node = node.left
            else:
                if node.right is None:
                    node.right = new_node
                    new_node.parent = node
                    return
                node = node.right

    def _isleaf(self, node):
        if node.left == None and node.right == None:
            return True
        return False
    
    def delete(self, data):

        node = self.root
        while node != None:
            if node.val == data:
                if self._isleaf(node): #leaf
                    parent = node.parent
                    
                    if parent.left == node:
                        parent.left = None
                       
                    else:
                        parent.right = None
                    return
                else:#not leaf
                    
                    #one child
                    if node.left!=None or node.right!=None:
                        parent = node.parent
                        child = node.left if node.left!=None else node.right
                        if parent.left == node:
                            parent.left = child
                        else:
                            parent.right = child
                        child.parent = parent
                    return

                    #two children
                
            elif node.val < data:
                node = node.right
            else:
                node = node.left
    
        
                    


        
        #non leaf ->has a left or right child

        #after delete substitute with one child and the parent of the child is gradfather
    def search(self, data):
        node = self.root
        while node!= None:
            if node.val == data:
                return True
            else:
                if node.val >= data:
                    node = node.left
                else:
                    node = node.right
        return False

    def _bst(self):
        pass
    
    def print_tree(self):
        self._travers_preorder(self.root)

    def _travers_inorder(self, node):
            
        if node != None:
            
            self._travers_inorder(node.left)
            print(node.val)
            self._travers_inorder(node.right)
        return
            

    def _travers_preorder(self, node):
        if node!= None:
            print(node.val)
            
            self._travers_preorder(node.left)
            
            self._travers_preorder(node.right)

        
    def _travers_postorder(self, node):   
    
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
l.delete(15)
l.print_tree()
print(l.search(15))


