class Solution:
    def carFleet(
        self, 
        target: int, 
        position: List[int], 
        speed: List[int]
    ) -> int:
        if len(position) == 1:
            return 1

        highway = {pos: (target - pos) / speed for pos, speed in zip(position, speed)}
        position = sorted(position, key=lambda x: -x)

        idx = 0
        while idx < len(position)-1:
            if highway[position[idx]] >= highway[position[idx+1]]:
                del position[idx+1]
            else:
                idx += 1

        return len(position)
        