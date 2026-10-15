class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or not t:
            return ""

        t_cnt = Counter(t)
        cur_cnt = Counter()
        have = 0
        need = len(t_cnt)
        shortest = ""

        l = 0
        for r, char in enumerate(s):
            cur_cnt[char] += 1

            if char in t_cnt and cur_cnt[char] == t_cnt[char]:
                have += 1

            while have == need:
                if not shortest or len(shortest) > (r - l):
                    shortest = s[l:r+1]

                cur_cnt[s[l]] -= 1
                if s[l] in t_cnt and cur_cnt[s[l]] < t_cnt[s[l]]:
                    have -= 1
                l += 1            
            
        return shortest