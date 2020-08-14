
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.current_index = 0
    
    def append(self, item):
        
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        
        else:
            if self.current_index < self.capacity:
                self.storage[self.current_index] = item
                self.current_index = (self.current_index + 1) % self.capacity
    
    def get(self):
        return self.storage
       
        
