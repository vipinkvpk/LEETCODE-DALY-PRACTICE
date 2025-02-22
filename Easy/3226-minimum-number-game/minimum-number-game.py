# class Solution:
#     def numberGame(self, nums: List[int]) -> List[int]:
#         nums1=[]
#         while nums :
#             alice_value=min(nums)
#             nums.remove(alice_value)
#             bobs_value=min(nums)
#             nums.remove(bobs_value)
#             nums1.append(bobs_value)
#             nums1.append(alice_value)      
#         return nums1
            
    
            

        

# ==========================================
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        target = []  # This will store the appended elements from all rounds
        
        # Process rounds until nums is empty
        while nums:
            # Check if there are at least 2 elements remaining, 
            # since we remove two each round.
            if len(nums) >= 2:
                alice_value = min(nums)
                nums.remove(alice_value)
                bobs_value = min(nums)
                nums.remove(bobs_value)
                
                # Bob's value is appended first, then Alice's
                target.append(bobs_value)
                target.append(alice_value)
            else:
                # If there's only one element left (shouldn't happen with even length),
                # you could choose to break or handle it accordingly.
                break
        
        return target
