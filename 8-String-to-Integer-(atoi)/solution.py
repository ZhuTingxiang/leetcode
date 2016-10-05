import re
pattern = re.compile("^[+-]?[0-9]+")

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        new_int = 0
        str = str.strip()
        if str!="":
            match = pattern.match(str)
            if match is not None:
                new_int = int(match.group())
            return max(min(new_int, 2147483647), -2147483648)
        return 0
            
           
            
        
    
        