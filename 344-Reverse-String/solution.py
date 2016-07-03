class Solution(object):
    def reverseString(self, s):
        s = list(s)
        for i in range(0,len(s)/2):
            tmp = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = tmp
        return ''.join(s)
        """
        :type s: str
        :rtype: str
        """