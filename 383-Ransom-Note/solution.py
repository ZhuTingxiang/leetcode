class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in ransomNote:
            for j in magazine:
                if i == j:
                    ransomNote.remove(i)
                    ransomNote.remove(j)
                else:
                    return False
        return True