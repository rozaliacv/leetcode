class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=1
        while(i<len(nums)):
            j=i
            while(j<len(nums) and nums[j-1]==nums[j]):
                nums.pop(j)
            i+=1
        return len(nums)
