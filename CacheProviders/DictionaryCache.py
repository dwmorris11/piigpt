import time
import threading
from BaseCache import BaseCache

class DictionaryCache(BaseCache):
    def __init__(self, time_to_live = 600, time_to_destroy = 60):
        self.cache = {}
        self.time_to_live = time_to_live
        self.time_to_destroy = time_to_destroy

    def set(self, key, value):
        self.cache[key] = {"value": value, "time": time.time()}

    def get(self, key):
        return self.cache.get(key)["value"]

    def _initialize_destroyer(self):
        '''This method starts a thread to destroy the cache when it expires'''
        destroyer = threading.Thread(target=self._destroy)
        destroyer.start()

    def _destroy(self):
        '''This method destroys the cache when it expires'''
        while True:
            for key in self.cache:
                if time.time() - self.cache[key]["time"] > self.time_to_live:
                    del self.cache[key]
            time.sleep(self.time_to_destroy)
