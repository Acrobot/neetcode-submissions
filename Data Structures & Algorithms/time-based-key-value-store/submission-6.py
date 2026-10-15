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

        res = ""
        while l <= r:
            mid = (l + r) // 2
            
            if timestamps[mid] <= timestamp:
                res = self.store[key][timestamps[mid]]
                l = mid + 1
            else:
                r = mid - 1

        # print(f"l: {l}, r: {r}")

        return res