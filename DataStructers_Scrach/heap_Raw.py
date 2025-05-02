
"""
implementing min heap
build: gets array and makes a heap-consider the childeren are in n//2 and from 0 to n//2-1 are parents

"""

class myheap:
    def __init__(self, arr=None):
        self.heap = []
        if arr:
            self.build(arr)

        
    def build(self, arr):
        #building the heap buttom up for parents: 0 to n//2-1
        n = len(arr)
        self.heap = arr.copy()
        for parent_idx in range(n//2-1, -1, -1):
            self._stif_down(parent_idx)



    def _stif_up(self, i):
        parent = (i - 1) // 2
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[index]
            self._stif_up(parent)
       

   
    
    def _stif_down(self, i):
        #compare left, righ in swap case: stif down swaped child
        left_child = self._get_left_child(i)
        right_child = self._get_right_child(i)

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        

        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child


        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._stif_down(smallest)

    def _get_right_child(self, i):
        return 2 * i + 2
    
    def _get_left_child(self, i):
        return 2 * i + 1
    
    
    def insert(self, val):
        self.heap.append(val)
        self._stif_up(len(self.heap)-1)

    def extract_min(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        

        
        
  