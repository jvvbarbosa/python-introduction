from operator import itemgetter 

EmptyQueue = []

class EmptyQueue(Exception):
        pass
    
    
class PriorityQueue():
    pass

    def add(self, a, b=2):
        if (b > 4) or ( b < 0):
            raise ValueError('Priority out of bounds', b)
        elif not isinstance(b, int):
            raise TypeError('Priority must be an integer. Received', type(b), b)
        
        try:
            int(b)
        except ValueError:
            raise TypeError
            
        self._q.append((a,b))
        self._q.sort(key=itemgetter(1))
        
    def __init__(self):
        self._q = []
 
    def __len__(self):
        return len(self._q)
        
    def pop(self):
        try:
            return self._q.pop(0)[0]
        except IndexError:
            raise EmptyQueue('There are no elements in the queue')