class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = version1.split('.')
        version2 = version2.split('.')
        for i in range(0,min(len(version1),len(version2))):
            if int(version1[i]) > int(version2[i]):
                return 1
            if int(version1[i])<int(version2[i]):
                return -1
        if len(version1) > len(version2):
            for i in version1[len(version2):]:
                if int(i) != 0:
                    return 1
            return 0
        if len(version1) < len(version2):
            for i in version2[len(version1):]:
                if int(i) != 0:
                    return -1
            return 0
    
        return 0
            
       