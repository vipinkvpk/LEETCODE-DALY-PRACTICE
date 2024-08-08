class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        Returns a new array that is the concatenation of two nums arrays.

        Args:
            nums: The input array.

        Returns:
            The concatenated array.
        """
        n =len(nums)
        ans=[0]*(2*n) # Create an array of zeros with double the length
# Fill the first half of ans with nums
        for  i in range(n):
            ans[i]=nums[i]
    # Fill the second half of ans with nums
        for i in range(n):
            ans[i+n]=nums[i]
        return ans
        