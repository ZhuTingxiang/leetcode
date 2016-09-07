class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return str(1)
        if n == 1:
            return str(1)
        s = self.countAndSay(n-1)
        count = 1
        result =''
        for i in range(0,len(s)-1):
            if s[i+1] == s[i]:
                count += 1
                continue
            else:
                result = result + str(count) + s[i]
                count = 1
        result = result + str(count) + s[len(s)-1]
        return result
                
            