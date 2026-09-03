class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                height = min(heights[j],heights[i])
                length = j - i
                res = max(res, height*length)
                
        return res
