class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1,dict2 = {},{}
        for index,char in enumerate(s):
            if char in dict1:
                if dict1[char] != t[index]:
                    print "1"
                    return False
            else:
                dict1[char] = t[index]
        for index,char in enumerate(t):
            if char in dict2:
                if dict2[char] != s[index]:
                    print "2"
                    return False
            else:
                dict2[char] = s[index]
        return True
        
            
        