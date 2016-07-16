class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        for val in nums:
            nums[i] = val
            nums.remove(val)
            i += 1
        print i
        return i
        
        """
        :type nums: List[int]
        :rtype: int
        """