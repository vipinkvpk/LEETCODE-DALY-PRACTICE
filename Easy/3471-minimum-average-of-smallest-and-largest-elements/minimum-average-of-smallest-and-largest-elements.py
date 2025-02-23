class Solution:
    def minimumAverage(self, nums: List[int]) -> float:

        averages=[]
        leng=int(len(nums)/2)
        for num in range(leng):
            smallest=min(nums)
            largest=max(nums)
            avg=(smallest+largest)/2
            averages.append(avg)
            nums.remove(smallest)
            nums.remove(largest)
            

        return min(averages)
            

        