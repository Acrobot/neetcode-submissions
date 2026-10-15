from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_cnt = Counter(t)
        cur_cnt = Counter()
        shortest = ""

        l = 0
        for r, char in enumerate(s):
            cur_cnt[char] += 1

            if char in t_cnt:
                while cur_cnt[s[l]] > t_cnt[s[l]]:
                    cur_cnt[s[l]] -= 1
                    l += 1

            for orig_c, cnt in t_cnt.items():
                if cur_cnt[orig_c] < cnt:
                    break
            else:
                if not shortest or len(shortest) > (r - l):
                    shortest = s[l:r+1]
            
        return shortest
