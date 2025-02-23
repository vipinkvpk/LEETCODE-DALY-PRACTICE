#

# class Solution:
#     def minimumAverage(self, nums: List[int]) -> float:

#         averages=[]
#         leng=int(len(nums)/2)
#         for num in range(leng):
#             smallest=min(nums)    # Find minimum element in nums (O(n))
#             largest=max(nums)     # Find maximum element in nums (O(n))
#             avg=(smallest+largest)/2
#             averages.append(avg)
#             nums.remove(smallest) # Remove smallest (O(n))
#             nums.remove(largest)  # Remove smallest (O(n))

#         return min(averages)     # Find min in averages (O(n/2))

# current solution's complexity: O(n²)




# =======================================================================
# Potential optimized solution: O(n log n) using sorting and two pointers.

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()  # Sort the array once, O(n log n)
        averages = []
        left, right = 0, len(nums) - 1
        
        # There will be n/2 rounds, where n is the original length
        while left < right:
            avg = (nums[left] + nums[right]) / 2  # Compute the average of the smallest and largest
            averages.append(avg)
            left += 1   # Move from the left end
            right -= 1  # Move from the right end
        
        # Return the minimum average from all rounds
        return min(averages)


            




