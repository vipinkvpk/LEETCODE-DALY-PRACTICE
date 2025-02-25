class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        res=""
        words=s.split()       # Splitting the string into words. O(n) time.
        tr=words[:k]          # Slicing the first k words. O(k) time.
        res+=" ".join(tr)     # Joining the k words into a single string. O(n) time.
        return res



# =================================================

# Complexity Analysis:
# Time Complexity:

# Splitting the string takes O(n), where n is the length of the string.
# Slicing takes O(k), but since k ≤ number of words, it is bounded by O(n) in the worst case.
# Joining the words takes O(n) (total length of the selected words).
# Overall, the time complexity is O(n).
# Space Complexity:

# You use additional space to store the list of words and the resulting string.
# Overall space complexity is O(n).


# Optimizations:
# Eliminate Unnecessary Variables:
# You don't really need the res variable. You can return the result of " ".join(words[:k]) directly.
# Combine Steps:
# You can combine splitting, slicing, and joining in one line.


# class Solution:
#     def truncateSentence(self, s: str, k: int) -> str:
#         return " ".join(s.split()[:k])


# Explanation:
# s.split() splits the sentence into a list of words.
# s.split()[:k] slices the list to keep only the first k words.
# " ".join(...) joins these words with a space in between to form the truncated sentence.
# This one-liner achieves the same result with minimal code and is efficient (O(n) time).
# This is likely the most optimized solution in terms of code simplicity and efficiency for this problem.
