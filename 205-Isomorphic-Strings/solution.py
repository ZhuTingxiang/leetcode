class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1,dict2 = {},{}
        for index,char in enumerate(s):
            if char not in dict1 and t[index] not in dict1.values():
                dict1[char] = t[index]
            else:
                if dict1.get(char) != t[index]:
                    return False
        return True
        
            
        