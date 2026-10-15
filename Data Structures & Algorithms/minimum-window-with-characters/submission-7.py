from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or not t:
            return ""

        t_cnt = Counter(t)
        cur_cnt = Counter()
        shortest_l, shortest_len = 0, 0

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
                if not shortest_len or shortest_len > (r - l):
                    shortest_l = l
                    shortest_len = (r - l + 1)
            
        return s[shortest_l:shortest_l + shortest_len]
