class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        
        potential_starts = set(
            x for x in num_set 
            if x - 1 not in num_set
        )

        longest_sequence = 0

        for start in potential_starts:
            seq_len = 0
            current_num = start

            while current_num in num_set:
                seq_len += 1
                current_num += 1
            
            longest_sequence = max(longest_sequence, seq_len)

        return longest_sequence