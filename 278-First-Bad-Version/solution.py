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
        first = 0
        n = (first+last) //2
        while last > first:
            n = (last+first)/2
            if isBadVersion(n):
                last = n
            else:
                first = n+1
        return first
                
            
            
        
                
        