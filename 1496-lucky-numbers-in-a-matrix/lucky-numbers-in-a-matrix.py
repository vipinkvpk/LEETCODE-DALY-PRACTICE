class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        lucky_nums = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                current = matrix[row][col]
                if current == min(matrix[row]) and current == max([matrix[i][col] for i in range(len(matrix))]):
                    lucky_nums.append(current)
        return lucky_nums