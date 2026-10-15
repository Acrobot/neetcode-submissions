class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1

        highway = {pos: speed for pos, speed in zip(position, speed)}
        position = sorted(position, reverse=True)

        fleets = 1
        previous_time = (target - position[0]) / highway[position[0]]
        for pos in position[1:]:
            car_speed = highway[pos]
            remaining_time = (target - pos) / car_speed

            if remaining_time > previous_time:
                fleets += 1
                previous_time = remaining_time

        return fleets
        