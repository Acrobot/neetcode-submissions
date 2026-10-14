class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        l_idx = 0
        r_idx = len(s) - 1

        while l_idx < r_idx:
            l_char, r_char = s[l_idx], s[r_idx]

            if not l_char.isalnum():
                l_idx += 1
                continue
            elif not r_char.isalnum():
                r_idx -= 1
                continue
            else:
                if l_char != r_char:
                    return False
                l_idx += 1
                r_idx -= 1
        
        return True