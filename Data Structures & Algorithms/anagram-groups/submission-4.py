from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for text in strs:
            letters = frozenset(Counter(text).items())
            if letters in groups:
                groups[letters].append(text)
            else:
                groups[letters] = [text]
        
        return [x for x in groups.values()]
        