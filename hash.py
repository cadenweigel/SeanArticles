class HashTable:
    def __init__(self, size=5000):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        """Generate a hash for a given key."""
        return hash(key) % self.size

    def set(self, key, value):
        """Insert or update the key-value pair."""
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key):
        """Retrieve the value for the given key. Raises KeyError if not found."""
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(f"Key '{key}' not found")

    def delete(self, key):
        """Remove the key-value pair. Raises KeyError if not found."""
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

        raise KeyError(f"Key '{key}' not found")

    def __contains__(self, key):
        """Support 'in' operator."""
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}({self.table})"
