class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 1
        while n>1:
            if n%2 == 0:
                return myPow(x,n/2)**2
            else:
                return myPow(x,n-1)*n
                
        
        
            
            
            