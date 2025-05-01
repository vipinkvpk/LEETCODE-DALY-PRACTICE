class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())

        







# BRUTE FORCE
# class Solution:
#     def countSegments(self, s: str) -> int:
#         count=0
#         string1=s.split()
#         for ch in string1:
#             count+=1 
#         return count