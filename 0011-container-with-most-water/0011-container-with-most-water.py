from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1  # two pointers
        max_area = 0  # store the maximum area found
        
        while l < r:
            # calculate current area
            area = (r - l) * min(height[l], height[r])
            # update max_area if this area is larger
            max_area = max(max_area, area)
            
            # move the pointer pointing to the shorter line
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return max_area
