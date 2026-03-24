class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        # list1=[]
        # list2=[]
        # list3=[]
        # for num in nums1:
        #     if num not in nums2 and num not in list1:
        #         list1.append(num)
        # for num2 in nums2:
        #     if num2 not in nums1:
        #         list2.append(num2)
        # list3.append(list1)
        # list3.append(list2)

        # return list3
        lst=[]
        unique1=set(nums1)
        unique2=set(nums2)
        unidiff1=unique1-unique2 
        unidiff2=unique2-unique1
        list1=list(unidiff1)
        list2=list(unidiff2)
        lst.append(list1)
        lst.append(list2)
        return lst