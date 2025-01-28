class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        largest=candies[0]
        largest=max(candies)
        for i in candies:
            # if i > largest:
            #     largest= i
            if (i+extraCandies) >= largest:     
                result.append(True)
            else:
                result.append(False)
        return result
            
        