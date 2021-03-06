from collections import deque
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.d = deque()
        

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
        if not self.empty():
            self.d.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if not self.empty():
            return self.d[-1]
        else:
            return None
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.d) == 0
        