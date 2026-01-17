class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        totalsum= sum(nums)
        leftsum=0
        answer=[]
        for i in range(len(nums)):
            rightsum= totalsum-leftsum-nums[i]
            answer.append(abs(leftsum-rightsum))
            leftsum += nums[i]
        return answer

        