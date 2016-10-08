import collections
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.d =  collections.deque()
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.d.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        if self.d:
            self.d.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.d:
            return self.d[-1]
        else:
            return None
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.d
        