class TimeMap:

    def __init__(self):
        self.store = defaultdict(lambda: defaultdict(str))

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        timestamps = list(self.store[key].keys())

        if not timestamps:
            return ""

        l = 0
        r = len(timestamps) - 1

        mid = 0
        while l < r:
            mid = (l + r + 1) // 2
            # print(f"mid: {mid}, l: {l}, r: {r}")

            if timestamps[mid] == timestamp:
                return self.store[key][timestamps[mid]]
            elif timestamps[mid] > timestamp:
                r = mid - 1
            else:
                l = mid

        # print(f"l: {l}, r: {r}")

        return self.store[key][timestamps[l]] if timestamps[l] <= timestamp else ""