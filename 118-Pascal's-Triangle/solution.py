class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        result = []
        if numRows == 1:
            result.append([1])
            return result
        if numRows == 2:
            result = self.generate(1)
            result.append([1,1])
            return result
        lastLine = []
        lastLine.append(1)
        result.append(self.generate(numRows-1))
        priorLine = result[len(result)-1]
        for index,char in enumerate(priorLine):
            if index < len(priorLine)-1:
                sum = []
                sum.append(char)
                sum.append(priorLine[index+1])
                print "sum",sum
                lastLine.append(sum)
        lastline.append(1)
        result.append(lastline)
        return result
                
                
            
            