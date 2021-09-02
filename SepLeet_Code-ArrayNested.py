class Solution(object):
    def arrayNesting(self, nums):
        n = len(nums)
        visited = [False] * n
        ans = 0
        for x in nums:
            cnt = 0
            while not visited[x]:
                cnt += 1
                visited[x] = True
                x = nums[x]
            ans = max(ans, cnt)
                
        return ans
