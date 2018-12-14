class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        given_num = x
        num = 0
        while (x > 0):
            rem = x % 10
            x = x/10
            num = num*10 +rem
        if (given_num == num):
            return True
        else:
            return False