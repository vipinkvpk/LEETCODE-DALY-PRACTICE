class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums1=[]
        while nums :
            alice_value=min(nums)
            nums.remove(alice_value)
            bobs_value=min(nums)
            nums.remove(bobs_value)
            nums1.append(bobs_value)
            nums1.append(alice_value)      
        return nums1
            
    
            

        