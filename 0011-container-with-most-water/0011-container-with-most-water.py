class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_cap = 0

        
        while i < j:

            cap = (j - i) * min(height[i], height[j])
            max_cap = max(cap, max_cap)

            if (height[i] < height[j]):
                i += 1
            else :
                j -= 1
        return max_cap