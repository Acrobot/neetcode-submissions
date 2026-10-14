class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        ptr = 0

        longest = 0
        current_chars = {}

        while ptr < len(s):
            if s[ptr] in current_chars:
                start = max(current_chars[s[ptr]] + 1, start)

            current_chars[s[ptr]] = ptr
            
            longest = max(longest, ptr - start + 1)
            ptr += 1

        return longest