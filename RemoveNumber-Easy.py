class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in nums[::]:
            if i == val:
                del nums[nums.index(i)]
        
        return len(nums)
  
