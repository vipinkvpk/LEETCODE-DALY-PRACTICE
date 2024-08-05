class Solution:
    def climbStairs(self, n: int) -> int:

        """
        Calculates the number of distinct ways to climb a staircase with n steps.

        Args:
            n: The number of steps in the staircase.

        Returns:
            The number of distinct ways to climb the staircase.
        """

        # Base cases:
        if n == 1:
            return 1  # Only one way to climb 1 step
        if n == 2:
            return 2  # Two ways to climb 2 steps

        # Create a list to store the number of ways to climb each step
        ways = [0] * (n + 1)

        # Initialize the first two steps
        ways[1] = 1
        ways[2] = 2

        # Calculate the number of ways for each step
        for i in range(3, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2] 

        # Return the number of ways to climb the entire staircase
        return ways[n]       