class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        length = 0
        if not s:
            return 0
        str = list(s)
        for i in str:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        max_even = 0
        for x in dict:
            if dict[x]/2>0:
                length += dict[x]/2 *2
        return length+1 if length < len(str) else length
            
            