class Solution(object):
    def addDigits(self, num):
        result = 0
        if num >= 10:
            while result == 0 or result >= 10:
                if result != 0:
                    num = result
                    result = 0
                while num/10 > 0:
                    result += num % 10
                    num = num/10
                result += num
            return result
        else:
            return num