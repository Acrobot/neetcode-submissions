class LRUCache:

    def __init__(self, capacity: int):
        self.storage = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        # print(f"get: {key}, storage: {self.storage}, ret: {self.storage.get(key, -1)}")
        item = self.storage.get(key)
        if item:
            del self.storage[key]
            self.storage[key] = item
        return item if item is not None else -1

    def put(self, key: int, value: int) -> None:
        # print(f"k: {key}, v: {value}, {self.storage}, cap: {self.capacity}")
        if key in self.storage:
            del self.storage[key]
        else:
            self.capacity -= 1

            if self.capacity < 0:
                old_key = next(iter(self.storage))
                del self.storage[old_key]
                self.capacity = 0

        self.storage[key] = value
