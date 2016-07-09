class Solution(object):
    def isPowerOfThree(self, n):
        if n <1:
            return False;
        else:
            while n/3!=1:
                n=n/3
            if n % 3!= 0:
                return False
            else:
                return True
        """
        :type n: int
        :rtype: bool
        """
        