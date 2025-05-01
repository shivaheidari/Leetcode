"""
Design a data structure to track the latest stock prices and support the following operations:

update(timestamp: int, price: int): Record a new price for the stock at the given timestamp.

If timestamp already exists, overwrite the old price with the new price.

current(): Return the latest price (the one with the highest timestamp).

maximum(): Return the highest price recorded so far.

minimum(): Return the lowest price recorded so far.

All operations should run in O(1) average time complexity (except update(), which can be O(log n) or better).

Assume timestamps are strictly increasing (like in real-time systems), but update() may still overwrite existing timestamps.

"""
import heapq

class StockTracker_naive():
    def __init__(self):
        self.price = 0
        self.timestamp = 0
        self.track= {} 
        

    def update(self, timestamp, price): #
        self.timestamp = timestamp
        self.price = price
        self.track[timestamp] = price
        return self.track
    
    def current(self):

        sorted_keys = sorted(self.track.items())
        #sort by keys
        max_item = sorted_keys[-1][1]
        return max_item
    
    def maximum(self):
        sorted_prices = sorted(self.track.items(), key= lambda item: item[1])
        max_item = sorted_prices[-1][1]
        return max_item


"""
we should use heap for updata and search. why? it is more efficeint. 
In the navie solution everything in best case is nlogn. By choosing heap as an efficient datastructure we can do the operations more efficient.

"""
class StockTracker():
        def __init__(self):
            self.prices = {}
            self.min_heap = []
            self.max_heap = []
            
    
        def update(self, timestamp, price):
             #overwrite and add to track
             if timestamp in self.prices:
                  old_price = self.prices[timestamp]


             self.prices[timestamp] = price
             heapq.heappush(self.min_heap, price)
             heapq.heappush(self.max_heap, -price)

        def current(self):
             last_time = max(self.prices.keys())
             return self.prices[last_time]
        
        def maximum(self):
             
             return self.max_heap[0]
        
        def minimum(self):
             return self.min_heap[0]



    
tr = StockTracker()
print(tr.update(1, 1000))
print(tr.update(2, 1004))
print(tr.update(3, 1002))
print(tr.current())
print(tr.maximum())
print(tr.minimum())
    


"""
-------------------------Taking message----------

dictionary sort: 

    by value: sorted_by_values_desc = sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
    by key: sorted_keys = sorted(self.track.items())) 





"""