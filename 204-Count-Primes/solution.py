
def isPrime(i):
    if i < 2:
        return False
    elif i == 2:
        return True
    else:
        for j in range(2 ,i):

            if i% j == 0:
                print "i%j",i%j
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
                print "i",i
                if isPrime(i):
                    print "isprime"
                    count += 1
        return count
