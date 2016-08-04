
def isPrime(i):
    if i < 2:
        return False
    elif i == 2:
        return True
    else:
        for j in range(2 ,i):
            if i% j == 0:
                return False
        return True

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        if n <= 2:
            return 0
        if n == 3:
            return 1
        else:
            for i in range(2,n):
                if isPrime(i):
                    count += 1
        return count
