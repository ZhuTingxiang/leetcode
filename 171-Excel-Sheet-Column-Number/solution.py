class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i,num in enumerate(reversed(s)):
            result += pow(26,i)*(ord(num) % ord('A')+1)
        return result