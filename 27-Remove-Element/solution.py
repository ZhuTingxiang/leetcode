class Solution(object):
    def removeElement(self, nums, val):
        ori_len = len(nums)
        j = 0
        for i in range(0,len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j+= 1
        print j
        return j
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        