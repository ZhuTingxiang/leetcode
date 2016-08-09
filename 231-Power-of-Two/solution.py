class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        while n/2 !=1:
            if n%2 == 0:
                n = n/2
            else:
                return False
        if n/2 == 1 and n%2 == 0:
            return True
        else:
            return False
        