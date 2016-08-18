class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict={}
        for index,char in enumerate(s):
            if char not in dict1 and t[index] not in dict.values():
                dict1[char] = t[index]
            else:
                if dict.get(char) != t[index]:
                    return False
        return True
        
            
        