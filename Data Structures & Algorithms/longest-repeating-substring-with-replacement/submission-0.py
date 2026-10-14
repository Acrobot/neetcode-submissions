class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        longest = 0

        max_frequency = 0
        l = 0

        for r, char in enumerate(s):
            counts[char] += 1
            max_frequency = max(max_frequency, counts[char])

            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest