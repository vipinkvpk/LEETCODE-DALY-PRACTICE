class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        result=[]
        n=len(height)
        for i in range(1,n):
            if height[i-1] > threshold:
                result.append(i)
        return result       