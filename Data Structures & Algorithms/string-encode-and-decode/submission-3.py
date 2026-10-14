class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(str(len(s)) + ' ' + s for s in strs)

    def decode(self, s: str) -> List[str]:
        chunks = []

        while s:
            num, _, rest = s.partition(' ')
            num = int(num)
            chunks.append(rest[:num])
            s = rest[num:]

        return chunks
