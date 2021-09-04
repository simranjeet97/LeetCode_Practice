class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return nums
        
        k = None
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                k = i
                
        if k is None:
            nums[:] = nums[::-1]  # if no such pair found, original array is descending
        else:
            l, r = k+1, len(nums)-1
            while l < r:
                m = l+(r-l+1)//2
                if nums[m] > nums[k]:
                    l = m
                else:
                    r = m-1
            nums[k], nums[l] = nums[l], nums[k]
            nums[k+1:] = nums[k+1:][::-1]
