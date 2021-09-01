class Solution(object):
    def removeDuplicates(self, nums):
        j=1
        for i in range(len(nums)-1):
            if (nums[i] != nums[i+1]):
                    nums[j]=nums[i+1]
                    j=j+1
        return j
