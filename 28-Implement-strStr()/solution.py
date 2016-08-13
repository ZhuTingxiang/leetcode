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
        if haystack == "":
            return -1
        else:
            for index_n,char_n in enumerate(needle):
                for index_h,char_h in enumerate(haystack):
                    if char_n == char_h:
                        if haystack[char_h,char_h + len_n + 1] == needle:
                            return char_h
        return -1
                        
                        