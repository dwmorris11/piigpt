import unittest
from unittest.mock import MagicMock
from Analyzers.AzureAIAnalyzer import AzureAIAnalyzer
from azure.ai.textanalytics import RecognizePiiEntitiesResult
from azure.ai.textanalytics import PiiEntity

class TestAzureAIAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = AzureAIAnalyzer(key="dummy_key", endpoint="dummy_endpoint")

    def test_analyze(self):
        # Test case 1: Analyze empty text list
        result = self.analyzer.analyze([])
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

        # Test case 2: Analyze non-empty text list
        mock_client = MagicMock()
        self.analyzer.client = mock_client
        mock_client.recognize_pii_entities.return_value = [
            RecognizePiiEntitiesResult(
                entities=[PiiEntity(text="John Doe", category="Person", subcategory=None, offset=0, length=8)],
                id="1",
                is_error=False,
                redacted_text=None
            )
        ]
        result = self.analyzer.analyze(["Hello, my name is John Doe."])
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], RecognizePiiEntitiesResult)
        self.assertEqual(result[0].entities[0].text, "John Doe")

    def test_scrub(self):
        # Test case 1: Scrub empty text list
        result = self.analyzer.scrub([])
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

        # Test case 2: Scrub non-empty text list
        mock_analyze = MagicMock(return_value=[
            RecognizePiiEntitiesResult(
                entities=[PiiEntity(text="John Doe", category="Person", subcategory=None, offset=0, length=8)],
                id="1",
                is_error=False,
                redacted_text="Hello, my name is [PERSON]."
            )
        ])
        self.analyzer.analyze = mock_analyze
        result = self.analyzer.scrub(["Hello, my name is John Doe."])
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], "Hello, my name is [PERSON].")

    def test_get_entities(self):
        # Test case 1: Get entities from empty text list
        result = self.analyzer.get_entities([])
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

        # Test case 2: Get entities from non-empty text list
        mock_analyze = MagicMock(return_value=[
            RecognizePiiEntitiesResult(
                entities=[PiiEntity(text="John Doe", category="Person", subcategory=None, offset=0, length=8)],
                id="1",
                is_error=False,
                redacted_text=None
            )
        ])
        self.analyzer.analyze = mock_analyze
        result = self.analyzer.get_entities(["Hello, my name is John Doe."])
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], list)
        self.assertEqual(len(result[0]), 1)
        self.assertIsInstance(result[0][0], PiiEntity)
        self.assertEqual(result[0][0].text, "John Doe")

if __name__ == '__main__':
    unittest.main()