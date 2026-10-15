class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or not t:
            return ""

        t_cnt = Counter(t)
        cur_cnt = Counter()
        have = 0
        need = len(t_cnt)
        shortest_l, shortest_len = 0, 0

        l = 0
        for r, char in enumerate(s):
            cur_cnt[char] += 1

            if char in t_cnt and cur_cnt[char] == t_cnt[char]:
                have += 1

            while have == need:
                if not shortest_len or shortest_len > (r - l + 1):
                    shortest_len = (r - l + 1)
                    shortest_l = l

                cur_cnt[s[l]] -= 1
                if s[l] in t_cnt and cur_cnt[s[l]] < t_cnt[s[l]]:
                    have -= 1
                l += 1            
            
        return s[shortest_l:shortest_l + shortest_len]