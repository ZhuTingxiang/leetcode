class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k != 0:
            k = k % len(nums)
            print k
            temp = nums[0:len(nums)-k]
            print temp
            nums[0:len(nums)-k] = nums[len(nums)-k:len(nums)]
            nums[k:len(nums)] = temp
            
            
        
                    
                    
                    
        