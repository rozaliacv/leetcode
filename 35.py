class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=len(nums)
        high = l-1
        low = 0
        indx1 =0
        indx2=0
        while(low<=high):
            mid = (low+high)/2
            indx1=indx2=mid
            if(nums[mid]==target):
                return mid
            elif(nums[mid]<target):
                low=mid+1
                indx1=indx1+1
            elif(nums[mid]>target):
                high=mid-1
                indx2=indx2-1
        if(indx1<indx2):
            return indx2
        else:
            return indx1