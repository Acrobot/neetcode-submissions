class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elems = set(nums)

        potential_starts = set(
            x for x in elems
            if x - 1 not in elems
        )

        longest_seq = 0

        for start in potential_starts:
            seq_len = 0
            current_num = start

            while current_num in elems:
                seq_len += 1
                current_num += 1

            longest_seq = max(longest_seq, seq_len)

        return longest_seq

        
        