class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.first_node = None
        self.second_node = None
        self.data = []
        
    def append(self, item):
        if len(self.data) == 0:
            self.first_node = 0
            return self.data.append(item)

        elif len(self.data) + 1 <= self.capacity:
            self.second_node = 1
            return self.data.append(item)

        else:
            self.data[self.first_node] = item
            self.first_node += 1
            if self.first_node + 1 > self.capacity:
                self.first_node = 0

    def get(self):
        return self.data