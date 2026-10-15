import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = list((num, idx) for idx, num in enumerate(nums[:k]))
        heapq.heapify_max(heap)

        out = [heap[0][0]]

        for idx, num in enumerate(nums[k:], start=k):
            heapq.heappush_max(heap, (num, idx))

            while heap[0][1] <= (idx-k):
                heapq.heappop_max(heap)

            out.append(heap[0][0])

        return out

