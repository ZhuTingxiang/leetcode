class Solution(object):
    def containsDuplicate(self, nums):
        len1 = len(nums)
        len2 = len(list(set(nums)))
        if (len1 == len2):
            return False
        else:
            return True

        """
        :type nums: List[int]
        :rtype: bool
        """