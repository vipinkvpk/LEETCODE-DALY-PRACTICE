class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        # shuffled_list=[' ']* len(s)
        shuffled_list = []
        for _ in range(len(s)):
            shuffled_list.append('')
        for ch,index in zip(s,indices):
            shuffled_list[index]=ch
        shuffled_string="".join(shuffled_list)
        return shuffled_string
        

# ============================================================
# class Solution:
#     def restoreString(self, s: str, indices: List[int]) -> str:
#         # Initialize an empty list to store characters at their correct positions
#         shuffled_list = [' '] * len(s)
        
#         # Loop through characters and corresponding indices
#         for char, index in zip(s, indices):
#             # Place each character at its correct position
#             shuffled_list[index] = char
        
#         # Join the list into a string to get the final shuffled string
#         shuffled_string = "".join(shuffled_list)
        
#         return shuffled_string
