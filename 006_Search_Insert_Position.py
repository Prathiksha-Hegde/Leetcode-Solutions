class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in nums:
            if (target > i):
                index_to_be_returned = nums.index(i) + 1
        if (target <= nums[0]):
            index_to_be_returned = 0
        return index_to_be_returned