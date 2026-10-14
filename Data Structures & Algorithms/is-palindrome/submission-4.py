class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        m = r // 2

        while l <= m and r >= m:
            if not s[l].isalnum():
                l += 1
                continue
            elif not s[r].isalnum():
                r -= 1
                continue
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1

        return True
        