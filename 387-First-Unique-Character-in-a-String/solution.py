class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 0
        list = []
        for index,char in enumerate(s):
            if index < len(s)-1:
                if char not in list:
                    if char in s[index+1:]:
                        list.append(char)
                        continue
                    else:
                        return index
                else:
                    continue
            if index == len(s)-1:
                if char not in list:
                    return index
                
                
        return -1
        
     