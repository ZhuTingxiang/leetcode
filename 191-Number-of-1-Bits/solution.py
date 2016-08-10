class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = bin(n)
        newString = str(b)
        count = 0
        for i in newString:
            if i == '1':
                count += 1
        return count