from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        out = []

        l = 0
        for idx, num in enumerate(nums):
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(idx)

            if l > q[0]:
                q.popleft()

            if (idx + 1) >= k:
                out.append(nums[q[0]])
                l += 1

        return out
        