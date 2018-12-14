class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack =[]
        for operations in ops:
            if operations=='+':
                stack.append(stack[-1]+stack[-2])
            elif operations =='C':
                stack.pop()
            elif operations =='D':
                stack.append(2*stack[-1])
            else:
                stack.append(int(operations))
        return sum(stack)