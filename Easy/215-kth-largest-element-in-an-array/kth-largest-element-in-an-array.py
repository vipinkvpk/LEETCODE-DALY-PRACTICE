import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min_heap = nums[:k]
        # heapq.heapify(min_heap)

        # for num in nums[k:]:
        #     if num > min_heap[0]:
        #         heapq.heappushpop(min_heap, num)
        # return min_heap[0]
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)

            # If the heap grows bigger than k, remove the smallest
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # The root of the heap is the kth largest element
        return min_heap[0]
        