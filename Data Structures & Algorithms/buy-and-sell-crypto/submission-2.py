class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_val = prices[0]
        max_val = 0
        result = 0

        for val in prices:

            if val < min_val:
                min_val = val
            result = val - min_val

            if result > max_val:
                max_val = result 

        return max_val
        