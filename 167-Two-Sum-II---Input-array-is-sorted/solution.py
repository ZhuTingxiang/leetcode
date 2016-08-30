class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        for index1,char1 in enumerate(numbers):
            for index2,char2 in enumerate(numbers[::-1]):
                if char1+char2 == target and index1 != len(numbers)-1-index2:
                    res.append(index1+1)
                    res.append(len(numbers)-index2)
                    return res
                    
            
        