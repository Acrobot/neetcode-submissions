class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_idx = {}

        longest = 0
        last_start = 0

        for idx, char in enumerate(s):
            if char in char_idx:
                last_start = max(char_idx[char]+1, last_start)
                print(f"'{char}' in idx, longest: {longest}, last_start: {last_start}")
            else:
                print(f"'{char}' not in indx, longest: {longest}")
            longest = max(idx - last_start + 1, longest)
            char_idx[char] = idx

        return longest
        