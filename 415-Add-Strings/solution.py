class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1,len2 = len(num1),len(num2)
        number1,number2 = 0,0
        if len1 > 1:
            for i in range(len1-1):
                number1 += 10**(len1-i-1)*int(num1[i])
        number1 += int(num1[-1])
        if len2 > 1:
            for i in range(len2-1):
                number2 += 10**int(len2-i-1)*int(num2[i])
        number2 += int(num2[-1])
        return str(number1+number2)
            
            