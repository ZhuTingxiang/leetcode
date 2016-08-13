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
        for j in result[len(result)-2]:
            print j
            sum = []
            sum.append(j)
            sum.append(j+1)
            lastLine.append(sum)
        lastline.append(1)
        result.append(lastline)
        return result
                
                
            
            