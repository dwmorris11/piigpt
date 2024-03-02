import unittest
import time
from CacheProviders.DictionaryCache import DictionaryCache

class TestDictionaryCache(unittest.TestCase):
    def setUp(self):
        self.cache = DictionaryCache()

    def test_set_and_get(self):
        # Test case 1: Set a value and retrieve it
        key = "key1"
        value = "value1"
        self.cache.set(key, value)
        result = self.cache.get(key)
        self.assertEqual(result, value)

        # Test case 2: Set a different value and retrieve it
        key = "key2"
        value = "value2"
        self.cache.set(key, value)
        result = self.cache.get(key)
        self.assertEqual(result, value)

    def test_delete(self):
        # Test case 1: Set a value, delete it, and try to retrieve it
        key = "key1"
        value = "value1"
        self.cache.set(key, value)
        self.cache.delete(key)
        result = self.cache.get(key)
        self.assertIsNone(result)

        # Test case 2: Set a different value, delete it, and try to retrieve it
        key = "key2"
        value = "value2"
        self.cache.set(key, value)
        self.cache.delete(key)
        result = self.cache.get(key)
        self.assertIsNone(result)

    def test_cache_expiration(self):
        # Test case 1: Set a value and wait for it to expire
        key = "key1"
        value = "value1"
        self.cache.set(key, value)
        time.sleep(self.cache.time_to_live + 1)
        result = self.cache.get(key)
        self.assertIsNone(result)

        # Test case 2: Set a different value and wait for it to expire
        key = "key2"
        value = "value2"
        self.cache.set(key, value)
        time.sleep(self.cache.time_to_live + 1)
        result = self.cache.get(key)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()