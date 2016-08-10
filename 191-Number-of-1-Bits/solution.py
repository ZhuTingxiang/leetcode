class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        length = len(n)
        string = str(n)
        if len(string)!=len(n):
            newString = 0*[len(n)-len(string)]+string
        
        if newString:
        count = 0
        for i in newString:
            print i
            if i == 1:
                count += 1
        return count