from os import getenv
import re
from Analyzers.AnalyzerType import AnalyzerType
from CacheProviders.BaseCache import BaseCache
from CacheProviders.DictionaryCache import DictionaryCache
from Analyzers.PIIEntity import PIIEntity
from Anonymizer import Anonymizer

class PIIScrubber:
    def __init__(self, analyzer_type: AnalyzerType, cache_provider: BaseCache = None, anonymizer = None):
        self.analyzer = self._get_analyzer(analyzer_type)
        self.cache_provider = cache_provider if cache_provider is not None else DictionaryCache()
        self.anonymizer = anonymizer if anonymizer is not None else Anonymizer(analyzer_type = analyzer_type)


    def _get_analyzer(self, analyzer_type: AnalyzerType):
        '''This method returns the analyzer based on the analyzer type'''
        if analyzer_type == AnalyzerType.AZURE:
            from Analyzers.AzureAIAnalyzer import AzureAIAnalyzer
            endpoint = getenv("AZURE_ENDPOINT")
            key = getenv("AZURE_KEY")
            if endpoint is None or key is None:
                raise ValueError("Azure endpoint and key are not set")
            return AzureAIAnalyzer(key, endpoint)
        else:
            raise ValueError("Analyzer type is not supported")

    def scrub(self, text):
        '''This method scrubs the text of PII and returns the redacted text'''
        return self.analyzer.scrub(text)

    def get_entities(self, text)  -> list[PIIEntity]:
        '''This method returns the PII entities in the text'''
        return self.analyzer.get_entities(text)

    def anonymize(self, entities: list[PIIEntity], text: str):
        '''This method anonymizes the text. It then stores the original text and the anonymized text in the cache.'''
        for entity in entities:
            anonymized_text = self.anonymizer.anonymize(entity.category, entity.length, entity.text)
            self.cache_provider.set(anonymized_text, entity.text)
            # Replace the original text with the anonymized text
            text = text.replace(entity.text, ":" + anonymized_text + ":")
        return text

    def deanonymize(self, text: str):
        '''This method deanonymizes the text. It then retrieves the original text from the cache.'''
        # Find all the anonymized text in the text
        anonymized_texts = re.findall(r':(.*?):', text)
        for anonymized_text in anonymized_texts:
            original_text = self.cache_provider.get(anonymized_text)
            # Replace the anonymized text with the original text and remove the angle brackets
            text = text.replace(":" + anonymized_text + ":", original_text)
        return text