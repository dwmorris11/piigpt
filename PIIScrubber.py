from os import getenv
from Analyzers import AnalyzerType
from CacheProviders import BaseCache, DictionaryCache

class PIIScrubber:
    def __init__(self, analyzer_type: AnalyzerType, cache_provider: BaseCache = None):
        self.analyzer = self._get_analyzer(analyzer_type)
        self.cache_provider = cache_provider if cache_provider is not None else DictionaryCache()

    def _get_analyzer(self, analyzer_type: AnalyzerType):
        '''This method returns the analyzer based on the analyzer type'''
        if analyzer_type == AnalyzerType.AZURE:
            from Analyzers import AzureAIAnalyzer
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

    def get_entities(self, text):
        '''This method returns the PII entities in the text'''
        return self.analyzer.get_entities(self.text)

    def anonymize(self, text):
        '''This method anonymizes the text. It then stores the original text and the anonymized text in the cache.'''
        return self.analyzer.anonymize(text)

    def deanonymize(self, text):
        '''This method deanonymizes the text. It then retrieves the original text from the cache.'''
        return self.cache_provider.get(self.anonymize(self.text))