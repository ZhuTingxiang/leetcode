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
        result = self.generate(numRows-1)
        priorLine = result[len(result)-1]
        for index,char in enumerate(priorLine):
            if index < len(priorLine)-1:
                sum = int(char) +  int(priorLine[index+1])
                lastLine.append(sum)
        lastLine.append(1)
        result.append(lastLine)
        return result
                
                
            
            