class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        a,b = 0,0
        same,s,g= [],[],[]
        for index,char in enumerate(guess):
            if secret[index] == guess[index]:
                a += 1
            else:
                s.append(secret[index])
                g.append(guess[index])
                        
        for i,c in enumerate(g):
            if g[i] in s:
                s.remove(g[i])
                b += 1
                
            
                            
        strr= ""
        strr = str(a)+"A"+str(b)+"B"
        return strr
        