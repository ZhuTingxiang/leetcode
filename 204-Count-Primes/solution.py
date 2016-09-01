from math import sqrt
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrime = [True for i in range(0,n)]
        count = 0
        for i in range(2,int(sqrt(n))+1):
            if isPrime[i] == False:
                continue
            for j in range(i*i,n,i):
                isPrime[j] = False
        for i in range(2,n):
            if isPrime[i] == True:
                count += 1
        return count
            
            
            
