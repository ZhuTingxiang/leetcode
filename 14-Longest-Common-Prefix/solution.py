class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        flag = True
        firstword = strs[0]
        longestPrefix = ''
        if len(strs) == 1:
            return firstword
        for i in range(0,len(firstword)):
            prefix = firstword[0:i+1]
            for j in strs:
                if j.startswith(prefix) is not True:
                    flag = False
            if flag == True:
                if len(prefix) > len(longestPrefix):
                    longestPrefix = prefix
        return longestPrefix
            
                
                
            
            
            