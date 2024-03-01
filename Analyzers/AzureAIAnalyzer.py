from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient, RecognizePiiEntitiesResult, DocumentError, PiiEntity
from Analyzers.BaseAnalyzer import BaseAnalyzer
from AnalyzerType import AnalyzerType

class AzureAIAnalyzer(BaseAnalyzer):
    def __init__(self, key, endpoint):
        self.client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))
        super()._load_configuration(AnalyzerType.AZURE)

    def analyze(self, text: list[str]) -> list[RecognizePiiEntitiesResult | DocumentError]:
        result: list[RecognizePiiEntitiesResult | DocumentError] = self.client.recognize_pii_entities(
                    documents=text,
                    categories_filter = self.config["categories_filter"] if "categories_filter" in self.config else None,
                    disable_service_logs =  self.config["disable_service_logs"] if "disable_service_logs" in self.config else None,
                    domain_filter = self.config["domain_filter"] if "domain_filter" in self.config else None,
                    language = self.config["language"] if "language" in self.config else None,
                    model_version = self.config["model_version"] if "model_version" in self.config else None,
                    show_stats = self.config["show_stats"] if "show_stats" in self.config else None,
                    string_index_type = self.config["string_index_type"] if "string_index_type" in self.config else None)
        docs = [doc for doc in result if not doc.is_error]
        return docs

    def scrub(self, text: list[str]) -> list[str]:
        docs = self.analyze(text)
        redacted_docs = [doc.redacted_text for doc in docs]
        return redacted_docs

    def get_entities(self, text: list[str]) -> list[list[PiiEntity]]:
        docs = self.analyze(text)
        entities = [doc.entities for doc in docs]
        return entities