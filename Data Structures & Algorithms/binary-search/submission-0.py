class Solution:
    def search(self, nums: List[int], target: int) -> int:
        fast = 0
        last = len(nums) - 1

        while fast <= last:
            middle = (fast + last) // 2

            # Check the VALUE at the middle index, not the index itself
            if target == nums[middle]: 
                return middle 
            elif target < nums[middle]:
                last = middle - 1 
            else:
                fast = middle + 1 
                
        return -1