import os
import toml
from Analyzers.AnalyzerType import AnalyzerType
from Analyzers.PIIEntity import PIIEntity

class BaseAnalyzer:
    def __init__(self, config):
        self.config = config

    def analyze(self, data):
        raise NotImplementedError("Analyze method is not implemented")

    def scrub(self, data):
        raise NotImplementedError("Scrub method is not implemented")

    def get_entities(self, data):
        raise NotImplementedError("Get entities method is not implemented")

    def _normalized_entities(self, entities: list[list[any]]) -> list[PIIEntity]:
        raise NotImplementedError("Normalized entities method is not implemented")

    def _load_configuration(self, analyzer_type: AnalyzerType):
        file_path = os.path.join(os.path.dirname(__file__), "../Config/analyzer_config.toml")
        if not os.path.exists(file_path):
            raise FileNotFoundError("The analyzer configuration file was not found")
        with open(file_path) as file:
            config = toml.load(file)
            self.config = config[analyzer_type.value]

