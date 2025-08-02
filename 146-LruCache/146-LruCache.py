# Last updated: 8/2/2025, 4:53:57 PM
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity
        self.leastRecent = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.leastRecent.remove(key)
            self.leastRecent.append(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.leastRecent.remove(key)
            self.leastRecent.append(key)
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                lru = self.leastRecent.pop(0)
                del (self.cache[lru])
            self.cache[key] = value
            self.leastRecent.append(key)

        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)