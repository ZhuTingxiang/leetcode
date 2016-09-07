class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        used = []
        
        magazine = list(magazine)
        for i in ransomNote:
            if i in magazine:
                used.append(i)
                magazine.remove(i)
            else:
                return False
        return True