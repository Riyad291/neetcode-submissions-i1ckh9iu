class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_v = 0
        l, r = 0, len(heights) - 1
        
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height
            
            max_v = max(max_v, area)
            
            # This replaces the inner while loops:
            if heights[l] < heights[r]:
                l += 1  # Move the shorter bar inward
            else:
                r -= 1  # Move the shorter bar inward
                
        return max_v