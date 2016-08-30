class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        index1, index2= 0, len(numbers)-1
        while index1!=len(numbers) and index2!=-1:
            if numbers[index1] + numbers[index2] == target:
                res.append(index1+1)
                res.append(index2+1)
                return res
            if numbers[index1] +  numbers[index2] > target:
                index2 -= 1
            else:
                index1 += 1
            
                    
            
        