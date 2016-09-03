class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = [0]*len(nums)
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        sum[0] = nums[0]
        sum[1] = max(nums[1],nums[0])
        for i in range(2,n):
            sum[i] = max(sum[i-1],sum[i-2]+nums[i])
        return sum[n-1]
        
            
            
                
                
        
                
            
        