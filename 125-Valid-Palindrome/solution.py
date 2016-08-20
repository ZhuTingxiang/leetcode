class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return True
        s = s.lower().replace(' ','')
        regex = re.compile('[a-z0-9]')
        s = regex.findall(s)
        s = ''.join(s)
        len(s)/2
        for index in range(0,len(s)/2):
            if s[index] != s[len(s)-1-index]:
                return False
        return True
            
        
        
        