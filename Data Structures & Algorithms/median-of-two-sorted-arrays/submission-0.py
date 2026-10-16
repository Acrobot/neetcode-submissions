
class Solution:
    def findMedianSortedArrays(
        self,
        nums1: list[int],
        nums2: list[int],
    ) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left_size = (m + n + 1) // 2

        l = 0
        r = m + 1

        while l < r:
            split1 = (l + r) // 2
            split2 = left_size - split1

            l1 = nums1[split1 - 1] if split1 > 0 else float("-inf")
            r1 = nums1[split1] if split1 < m else float("inf")
            l2 = nums2[split2 - 1] if split2 > 0 else float("-inf")
            r2 = nums2[split2] if split2 < n else float("inf")

            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return float(max(l1, l2))
            elif l1 > r2:
                r = split1
            elif l2 > r1:
                l = split1 + 1
