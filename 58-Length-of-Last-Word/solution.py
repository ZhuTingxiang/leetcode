class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = s.split()
        if len(l) >= 1:
            return len(l[len(l)-1])
        else:
            return 0