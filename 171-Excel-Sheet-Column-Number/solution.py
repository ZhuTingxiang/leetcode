class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 1
        # if len(s) == 1:
        #     result = ord(s[0]) % ord('A') + 1
        # else:
        result = 0
        for i in range(0,len(s)):
            result += 26**(len(s)-i-1)*(ord(s[i]) % ord('A')+1)
        return result