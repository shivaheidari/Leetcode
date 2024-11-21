class Hashtable_list:
    def __init__(self,size):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash(self,key):
        return hash(key)%self.size
    
    def insert(self,key,value):
        index = self.hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1]=value
                return
        self.table[index].append([key,value])
        
        

    def delete(self,key):
        index = self.hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return True
        return False

    def search(self,key):
        index = self.hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class Hashtable_linkedlist:
    def __init__(self,size):
        self.size = size
        self.table = [None]*size 

hash_table = Hashtable_list(5)
hash_table.insert("a",1)
hash_table.insert("b",2)
print(hash_table.delete("c"))
print(hash_table.search("a"))