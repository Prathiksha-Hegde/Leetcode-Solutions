class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list_values =[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.list_values.insert(len(self.list_values),x)
        

    def pop(self):
        """
        :rtype: void
        """
        self.list_values.pop()    
    
    def top(self):
        """
        :rtype: int
        """
        top_element = self.list_values[-1]
        return top_element
        

    def getMin(self):
        """
        :rtype: int
        """
        min_element = min(self.list_values)
        return min_element
        
        


