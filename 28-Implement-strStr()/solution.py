class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_n = len(needle)
        if len_n == 0:
            return 0
        else:
            for index_h,char_h in enumerate(haystack):
                if haystack[index_h:index_h + len_n] == needle:
                    return index_h
        return -1
                        
                        