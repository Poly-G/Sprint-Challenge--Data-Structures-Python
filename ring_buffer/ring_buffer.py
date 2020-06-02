class RingBuffer:
    def __init__(self, capacity):
        # set up the max
        self.capacity = capacity
        # keeping track of the current item
        self.current = 0
        # where we are storing the items
        self.data = [None]*capacity

    def append(self, item):
        # check to see if current is less than length
        if self.current < self.capacity:
            # use index to delete oldest element
            self.data.pop(self.current)
            # insert new element where oldest was removed
            self.data.insert(self.current, item)
            # increase current
            self.current = self.current + 1

            # at the end of the list, reset current to 0
            if self.current == self.capacity:
                self.current = 0

    def get(self):
        # initiate empty list
        answer = []
        # add to empty list if item is not None
        for i in self.data:
            if i != None:
                answer.append(i)
        return answer
