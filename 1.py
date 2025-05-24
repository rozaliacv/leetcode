class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            n=nums.index(i)
            num = nums[n+1:]
            for j in num:
                if(i+j==target):
                    return [ n, num.index(j)+n+1]
       

def main():
    nums = input().split()
    target = int(input())
    ret = Solution().twoSum(nums,target)
    print(ret)

if __name__ == "__main__":
    main()
