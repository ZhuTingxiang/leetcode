class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        else:
            last = self.getRow(rowIndex-1)
            line = [1]
            for i in range(0,len(last)-1):
                line.append(last[i]+last[i+1])
            line.append(1)
            print line
            return line
                
            
        