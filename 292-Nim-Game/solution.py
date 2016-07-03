class Solution(object):
    def canWinNim(self, n):
        if n< 4:
            return True
        elif n == 4:
            return False
        else:
            if n%4!=0:
                return True
            else:
                return False
        
        
        """
        :type n: int
        :rtype: bool
        """