class Solution:
    _DELIMITER = "#"

    def encode(self, strs: List[str]) -> str:
        return "".join(
            f"{len(text)}{self._DELIMITER}{text}" 
            for text in strs
        )

    def decode(self, s: str) -> List[str]:
        returned = []

        while s:
            number = s.find(self._DELIMITER)
            count = int(s[:number])

            text = s[number + 1 : number + 1 + count]
            returned.append(text)

            s = s[number + 1 + count:]

        return returned
