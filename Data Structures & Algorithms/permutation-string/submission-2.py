class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        orig_count = Counter(s1)
        current_count = Counter()

        for idx in range(len(s2)):
            if idx >= len(s1):
                current_count[s2[idx - len(s1)]] -= 1
            current_count[s2[idx]] += 1
            
            if current_count == orig_count:
                return True

        return False