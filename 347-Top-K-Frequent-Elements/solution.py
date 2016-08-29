class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        for i in nums:
            print i
            if not dict.has_key(i):
                dict[i] = 1
            else:
                dict[i] += 1
        dict = sorted(dict,key = dict.get,reverse = True)
        return dict[:k]
        
            
            
            
            
        