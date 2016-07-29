class Solution(object):
    def wordPattern(self, pattern, str):
        print str
        str_split = []
        for i in str.split():
            if i is not None:
                str_split.append(i)
        for n in range(0,len(pattern)-1):
            for m in range(n+1,len(pattern)):
                if pattern[n] == pattern[m]:
                    if str_split[n] != str_split[m]:
                        return False
                else:
                    if str_split[n] == str_split[m]:
                        return False
        return True










        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """