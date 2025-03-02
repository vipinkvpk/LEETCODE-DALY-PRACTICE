class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Slow pointer

        for i in range(len(nums)):  # Fast pointer iterates over the array
            if nums[i] != val:
                nums[k] = nums[i]  # Move non-val element to the front
                k += 1  # Move slow pointer ahead

        return k  # k is the count of remaining elements

        
        