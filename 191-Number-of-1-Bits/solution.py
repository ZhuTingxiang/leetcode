class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        str = ''
        str = str(n)
        count = 0
        for i in str:
            if i != 0:
                count += 1
        return count