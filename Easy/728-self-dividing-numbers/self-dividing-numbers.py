class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        # left_l= len(left)
        # right_l=len(right)
        # for i in range(left_l, right_l+1):
        #     for j in range(i):
        #         if (j%left_i[0] and j %right_i[1] )==0:
        #             return True

        return [num for num in range(left, right+1) if all(n!=0 and num % n ==0 for n in map(int, str(num)))]
        