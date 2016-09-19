class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <= -1:
            return False
        if x == 0:
            return True
        number_list = []
        while x >= 10:
            xx = x % 10
            x = x/10
            number_list.append(xx)
        number_list.append(x)
        for i in range(0,len(number_list)/2):
            if number_list[i] != number_list[len(number_list)-i-1]:
                return False
        return True
            
        
        