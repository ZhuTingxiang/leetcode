class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        a,b = 0,0
        same,almost = [],[]
        for index1,char1 in enumerate(secret):
            for index2,char2 in enumerate(guess):
                if char1 == char2:
                    if index1 == index2:
                        same.append(index2)
                        a += 1
        print same
         for index1,char1 in enumerate(secret):
             for index2,char2 in enumerate(guess):
                if char1 == char2:
                    print char1
                    if index2 not in same:
                        if index2 not in almost:
                            print index2
                            almost.append(index2)
                            b += 1
        strr= ""
        strr = str(a)+"A"+str(b)+"B"
        return strr
        