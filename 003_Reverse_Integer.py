class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = 0  
        flag = 0
        if x < 0:
            x = abs(x) 
            flag = 1
        while (x > 0):
            rem = x % 10;
            x = x/10;
            num = num*10+rem
          
        if flag == 1:  
            num  = num*-1
        if (-2**31 <num and num < 2**31 -1):
            num = num
        else:
            num = 0
        return num
        