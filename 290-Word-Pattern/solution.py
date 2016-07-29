class Solution(object):
    def wordPattern(self, pattern, str):

        str_split = []
        for i in str.split():
            if i is not None:
                str_split.append(i)
        if len(pattern) ==1:
            return True
        else:
            for n in range(0,len(pattern)-1):
                for m in range(n+1,len(pattern)):
                    if pattern[n] is None or pattern[m] is None:
                        print "ye"
                        return False
                    elif pattern[n] == pattern[m]:
                        if str_split[n] != str_split[m]:
                            print "a"
                            return False
                    elif str_split[n] == str_split[m]:
                                print n
                                print m
                                print "he"
                                return False
        return True

















        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """