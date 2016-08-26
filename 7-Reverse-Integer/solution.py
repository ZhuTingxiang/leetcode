class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        result = 0
        if x >= 0:
            result = int(s[::-1])
        else:
            result =int('-'+s[1:][::-1])
        return result if -2147483647 <= result <= 2147483647 else 0
            