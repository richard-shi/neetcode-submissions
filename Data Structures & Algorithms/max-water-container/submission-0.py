class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def volume(left, right):
            return min(heights[left], heights[right]) * (right - left)

        l, r = 0, len(heights) - 1
        max_vol = 0

        while l < r:
            vol = volume(l, r)
            max_vol = max(vol, max_vol)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] >= heights[r]:
                r -= 1
        
        return max_vol
            


        












        