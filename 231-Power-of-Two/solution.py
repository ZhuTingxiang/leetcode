class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n >1:
            if n %2 == 0:
                return self.isPowerOfTwo(n /2)
            else:
                return False
        if n == 1:
            return True
        if n <= 0:
            return False
       
        