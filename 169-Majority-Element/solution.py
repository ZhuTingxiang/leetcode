class Solution(object):
    def majorityElement(self, nums):
        size = len(nums)
        pool =[]
        for i in nums:
            if i not in pool:
                pool.append(i)
                if nums.count(i)>size/2:
                    return i

        
        """
        :type nums: List[int]
        :rtype: int
        """