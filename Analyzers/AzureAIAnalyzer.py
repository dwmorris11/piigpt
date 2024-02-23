import toml
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

class AzureAIAnalyzer:
    def __init__(self, key, endpoint):
        self.client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))
        self.config = None
        self._load_configuration()
    
    def _load_configuration(self):
        file_path = os.path.join(os.path.dirname(__file__), "analyzer_config.toml")
        if not os.path.exists(file_path):
            raise FileNotFoundError("The analyzer configuration file was not found")
        with open(file_path) as file:
            config = toml.load(file)
            self.config = config["AzureAIAnalyzer"]

    def analyze(self, text: list[str]):
        result = self.client.recognize_pii_entities(documents=text, language=self.config["language"], domain_filter=self.config["domain_filter"])
        docs = [doc for doc in result if not doc.is_error]
        return docs

    def scrub(self, text: list[str]):
        docs = self.analyze(text)
        redacted_docs = [doc.redacted_text for doc in docs]
        return redacted_docs

    def get_entities(self, text: list[str]):
        docs = self.analyze(text)
        entities = [doc.entities for doc in docs]
        return entities