class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        indexlist =[]
        if not magazine and ransomeNote:
            return False
        for index,char in enumerate(ransomNote):
            for index2,char2 in enumerate(magazine):
                if char == char2:
                    if index2 in indexlist:
                        if index2 is not len(magazine)-1:
                            continue
                        else:
                            return False
                    else:
                        indexlist.append(index2)
                        break
                else:
                    return False
        return True