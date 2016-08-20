import re
regex = re.compile('[a-z0-9]')
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return True
        s = s.lower().replace(' ','')
        s = regex.findall(s)
        s = ''.join(s)
        for i in range(0,len(s)/2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True
            
        
        
        