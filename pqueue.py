#from operator import itemgetter 

EmptyQueue = []

class EmptyQueue(Exception):
        pass
    
    
class PriorityQueue_very_slow():
    pass

    def add(self, a, b=2):
        if not (0 <= b <= 4):
            raise ValueError('Priority out of bounds', b)
        elif not isinstance(b, int):
            raise TypeError('Priority must be an integer. Received', type(b), b)
        
        try:
            int(b)
        except ValueError:
            raise TypeError
            
        if not self._q:
            self._q.append((a,b))
        else:
            ind = 0
            for val, prio in self._q:
                if prio > b:
                    break
            
                ind += 1
            self._q.insert(ind, (a, b))
        
    def __init__(self):
        self._q = []
 
    def __len__(self):
        return len(self._q)
        
    def pop(self):
        try:
            return self._q.pop(0)[0]
        except IndexError:
            raise EmptyQueue('There are no elements in the queue')
            
            

class PriorityQueue_fast():

    def add(self, a, b=2):
        if not (0 <= b <= 4):
            raise ValueError('Priority out of bounds', b)
        self._q[b].append(a)
            
        
    def __init__(self):
        self._q = ([],[],[],[],[])
 
    def __len__(self):
        return sum(map(len, self._q))
        
    def pop(self):
        for q in self._q:
            if q:
                return q.pop(0)
        else:
            raise EmptyQueue('There are no elements in the queue')
            
            
            
            
from collections import deque
class PriorityQueue():

    def add(self, a, b=2):
        if not (0 <= b <= 4):
            raise ValueError('Priority out of bounds', b)
        self._q[b].append(a)
            
        
    def __init__(self):
        #self._q = (deque(), deque(), deque(), deque(), deque()) 
        #self._q = tuple([deque() for _ in range(5)])
        self._q = tuple( deque() for _ in range(5) )#This is a bit faster because it doesnt create a list to then tuple it
 
    def __len__(self):
        return sum(map(len, self._q))
        
    def pop(self):
        for q in self._q:
            if q:
                return q.popleft()
        else:
            raise EmptyQueue('There are no elements in the queue')