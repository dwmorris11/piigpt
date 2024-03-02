import unittest
from Anonymizer import Anonymizer

class TestAnonymizer(unittest.TestCase):
    def setUp(self):
        self.anonymizer = Anonymizer()

    def test_anonymize_text(self):
        # Test case 1: Anonymize text with default entity type and length
        result = self.anonymizer.anonymize_text()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

        # Test case 2: Anonymize text with specified entity type and length
        result = self.anonymizer.anonymize_text(entity_type="email", length=10)
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 10)

    def test_anonymize_number(self):
        # Test case 1: Anonymize number with default entity type and length
        result = self.anonymizer.anonymize_number()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

        # Test case 2: Anonymize number with specified entity type and length
        result = self.anonymizer.anonymize_number(entity_type="phone", length=8)
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 8)

    def test_anonymize(self):
        # Test case 1: Anonymize with default entity type and length
        result = self.anonymizer.anonymize()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

        # Test case 2: Anonymize with specified entity type and length
        result = self.anonymizer.anonymize(entity_type="address", length=15)
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 15)

if __name__ == '__main__':
    unittest.main()