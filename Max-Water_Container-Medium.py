class Solution(object):
    def maxArea(self, height):
        max_area = 0
        # Left and right pointers
        left = 0
        right = len(height) - 1
        # Loop until the two pointers meet
        while left < right:
            # Shorter of the two lines
            shorter_line = min(height[left], height[right])
            max_area = max(max_area, shorter_line * (right - left))
            # If there is a longer vertical line present
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area