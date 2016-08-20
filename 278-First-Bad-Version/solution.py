# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        last = n
        for index in range(1,n):
            if isBadVersion(index-1) == False and isBadVersion(index) == True:
                return index
        
                
        