class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        MaxSum = nums[0]
        curr_sum = MaxSum
        for num in nums[1:]:
            temp = curr_sum + num
            curr_sum = temp if temp > num else num
            MaxSum = curr_sum if curr_sum > MaxSum else MaxSum
        return MaxSum
