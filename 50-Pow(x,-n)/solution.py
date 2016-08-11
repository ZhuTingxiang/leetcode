class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 1
        if n<0:
            return 1/self.myPow(x,-n)
        while n>1:
            if n%2 == 0:
                res = self.myPow(x,n/2)
                return  res*res
            else:
                return x * self.myPow(x,n-1)
                
        
        
            
            
            