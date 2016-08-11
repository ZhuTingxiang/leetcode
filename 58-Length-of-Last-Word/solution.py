class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s == '' or s == "":
            return 0
        l = s.split()
        return len(l[len(l)-1])