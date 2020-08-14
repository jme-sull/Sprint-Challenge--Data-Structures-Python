
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
    
    def append(self, item):
        
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        
        else:
            i = 0
            if i < self.capacity:
                self.storage[i] = item
                i += 1
                return i
            else:
                i= 0
                self.storage[i] =item
                return i
                

    def get(self):
       return self.storage
        
