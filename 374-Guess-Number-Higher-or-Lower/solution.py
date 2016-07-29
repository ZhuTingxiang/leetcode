# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if guess(n) == 0:
            return n
        g=(1+n)/2
        result = guess(g)
        small_num = 1
        big_num = n
        
        else:
            while result!=0:
                if result == -1:
                    big_num = g
                    g = (g+small_num)/2
                elif result == 1:
                        small_num = g
                        g=(big_num+g)/2
                    
                result = guess(g)
            return g


        
        