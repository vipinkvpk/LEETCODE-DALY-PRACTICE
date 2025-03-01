# class Solution:
#     def sortEvenOdd(self, nums: List[int]) -> List[int]:

        # even_values = []  # Stores values at even indices
        # odd_values = []   # Stores values at odd indices

        # for i in range(len(nums)):  # Loop through indices
        #     if i % 2 == 0:
        #         even_values.append(nums[i])  # Store even-indexed elements
        #     else:
        #         odd_values.append(nums[i])   # Store odd-indexed elements

        # even_values.sort()   # Sort even indices in ascending order
        # odd_values.sort(reverse=True) # Sort odd indices in descending order

        # # Place the sorted values back into their respective positions
        # even_index, odd_index= 0, 0
        
        # for i in range(len(nums)):
        #     if i%2==0:
        #         nums[i]=even_values[even_index]
        #         even_index=+1
        #     else:
        #         nums[i]=odd_values[odd_index]
        #         odd_index+=1
        # return nums
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even_values = [nums[i] for i in range(0, len(nums), 2)]
        odd_values = [nums[i] for i in range(1, len(nums), 2)]

        even_values.sort()  # Sort even indices in ascending order
        odd_values.sort(reverse=True)  # Sort odd indices in descending order

        # Place the sorted values back into their respective positions
        even_index, odd_index = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = even_values[even_index]
                even_index += 1
            else:
                nums[i] = odd_values[odd_index]
                odd_index += 1

        return nums
