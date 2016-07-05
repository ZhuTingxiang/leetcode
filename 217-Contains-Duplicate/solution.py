class Solution(object):
    def containsDuplicate(self, nums):
        len1 = len(nums)
        len2 = len(set(nums))
        return len1!=len2

        """
        :type nums: List[int]
        :rtype: bool
        """