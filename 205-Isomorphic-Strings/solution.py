class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        for index,char in enumerate(s):
            if char in dict or t[index] in dict:
                if dict[char] != t[index]:
                    return False
            else:
                # if t[index] in dict:
                #     return False
                dict[char] = t[index]
        return True
        
            
        