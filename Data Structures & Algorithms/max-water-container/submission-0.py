class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 2:
            return (min(heights[0], heights[1]))
        i = 0
        j = n - 1
        res = 0
        while i < j:
            area = min(heights[i], heights[j]) * (j - i)
            res = max(res, area)
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return res