class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1.0 / self.myPow(x,-n)
        if n == 0:
            return 1
        if n%2 == 0:
            res =self.myPow(x,int(n/2)) 
            return res*res
        else:
            return x * self.myPow(x,n-1)
                
        
        
            
            
            