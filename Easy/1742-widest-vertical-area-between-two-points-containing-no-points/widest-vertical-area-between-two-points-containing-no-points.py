class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x=[point[0] for point in points]
        x.sort()
        gaps=[x[i]-x[i-1] for i in range(1,len(x))]
        max_gap=max(gaps)
        return max_gap
