class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        x=0
        for i in range(len(nums)):
            if (val != nums[i]):
                nums[x] = nums[i]
                x+=1
        return x
        