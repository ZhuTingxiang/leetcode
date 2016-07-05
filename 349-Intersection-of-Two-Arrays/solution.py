class Solution(object):
    def intersection(self, nums1, nums2):
        result =[]
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        for i in nums1:
            for n in nums2:
                if i == n:
                    result.append(i)
        return result
        
        
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """