class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pairs=list(zip(heights,names))
        sorted_pairs=sorted(pairs, key=lambda x: x[0], reverse=True)
        sorted_names=[name for height, name in sorted_pairs]
        return sorted_names

      







# ===============================================================
# class Solution:
#     def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
#         # Step 1: Pair each name with its height using zip.
#         pairs = list(zip(heights, names))         # O(n)       
        
#         # Step 2: Sort the pairs in descending order by height.
#         # The key 'lambda x: x[0]' tells Python to sort by the height (first element of the tuple).
#         # 'reverse=True' sorts in descending order.
#         sorted_pairs = sorted(pairs, key=lambda x: x[0], reverse=True)  # O(n log n)
        
#         # Step 3: Extract the names from the sorted pairs.
#         sorted_names = [name for height, name in sorted_pairs]     # O(n)
        
#         return sorted_names

# # Example Usage:
# sol = Solution()
# print(sol.sortPeople(["Mary", "John", "Emma"], [180, 165, 170]))
# # Output: ["Mary", "Emma", "John"]



# # Thus, the overall time complexity is O(n log n), dominated by the sorting step.