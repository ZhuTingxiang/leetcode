class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if version1 == version2:
            return 0
        version1 = version1.split('.')
        version2 = version2.split('.')
        if version1[0] > version2[0]:
            return 1
        if version1[0] < version2[0]:
            return -1
        if version1[0] ==version2[0]:
            return 1 if version1[1] > version2[1] else -1
        return 0