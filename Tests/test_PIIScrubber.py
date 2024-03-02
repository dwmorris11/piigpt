import unittest
from unittest.mock import MagicMock
from PIIScrubber import PIIScrubber, AnalyzerType, PIIEntity

class TestPIIScrubber(unittest.TestCase):
    def setUp(self):
        self.scrubber = PIIScrubber(analyzer_type=AnalyzerType.AZURE)

    def test_scrub(self):
        # Test case 1: Scrub empty text
        result = self.scrubber.scrub("")
        self.assertEqual(result, "")

        # Test case 2: Scrub text with PII
        mock_analyzer = MagicMock()
        mock_analyzer.scrub.return_value = "Hello, my name is [PERSON]."
        self.scrubber.analyzer = mock_analyzer
        result = self.scrubber.scrub("Hello, my name is John Doe.")
        self.assertEqual(result, "Hello, my name is [PERSON].")

    def test_get_entities(self):
        # Test case 1: Get entities from empty text
        result = self.scrubber.get_entities("")
        self.assertEqual(result, [])

        # Test case 2: Get entities from text with PII
        mock_analyzer = MagicMock()
        mock_analyzer.get_entities.return_value = [
            PIIEntity(text="John Doe", category="Person", subcategory=None, offset=0, length=8)
        ]
        self.scrubber.analyzer = mock_analyzer
        result = self.scrubber.get_entities("Hello, my name is John Doe.")
        self.assertEqual(result, [
            PIIEntity(text="John Doe", category="Person", subcategory=None, offset=0, length=8)
        ])

    def test_anonymize(self):
        # Test case 1: Anonymize empty entities and text
        entities = []
        text = ""
        result = self.scrubber.anonymize(entities, text)
        self.assertEqual(result, "")

        # Test case 2: Anonymize entities in text
        entities = [
            PIIEntity(text="John Doe", category="Person", subcategory=None, offset=0, length=8)
        ]
        text = "Hello, my name is John Doe."
        mock_anonymizer = MagicMock()
        mock_anonymizer.anonymize.return_value = "ANONYMIZED"
        self.scrubber.anonymizer = mock_anonymizer
        result = self.scrubber.anonymize(entities, text)
        self.assertEqual(result, "Hello, my name is :ANONYMIZED:.")

    def test_deanonymize(self):
        # Test case 1: Deanonymize empty text
        result = self.scrubber.deanonymize("")
        self.assertEqual(result, "")

        # Test case 2: Deanonymize text with anonymized entities
        text = "Hello, my name is :ANONYMIZED:."
        mock_cache_provider = MagicMock()
        mock_cache_provider.get.return_value = "John Doe"
        self.scrubber.cache_provider = mock_cache_provider
        result = self.scrubber.deanonymize(text)
        self.assertEqual(result, "Hello, my name is John Doe.")

if __name__ == '__main__':
    unittest.main()