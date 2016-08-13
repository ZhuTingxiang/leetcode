class Solution(object):
    def intersect(self, nums1, nums2):
        d = dict()
        result = []
        if nums1 == [] or nums2 == []:
            return result
        for i in nums1:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] +=1
        for j in nums2:
            if j in dict:
                if dict[j] >=1:
                    result.append(j)
        return result
            
                    
                    
                
        
        
        