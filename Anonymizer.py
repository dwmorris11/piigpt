import random
import os
import toml
import exrex
from Analyzers import AnalyzerTypes

class Anonymizer:
    def _init_(self, config_file_path = None, analyzer_type: AnalyzerTypes = AnalyzerTypes.AZURE):
        if config_file_path is None:
            file_path = os.path.join(os.path.dirname(__file__), "anonymizer_config.toml")
        self.config = None
        self.analyzer_type = analyzer_type.value
        self._load_configuration(file_path)

    def _load_configuration(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError("The anonymizer configuration file was not found")
        with open(file_path) as file:
            config = toml.load(file)
            self.config = config[self.analyzer_type]

    def anonymize(self, entity_type = None, length_match = False, length = None, data = None):
        pass

    def _anonymize_text(self, entity_type = None, length = None):
        if entity_type == None:
            text_length = random.randint(1, 10) if length == None else length
            return f"{''.join([chr(random.randint(97, 122)) for _ in range(text_length)])}"
        else:
            pattern = self.config[entity_type] if entity_type in self.config else self.config["default"]
            return exrex.getone(pattern)

    def _anonymize_number(self, entity_type = None, length = None):
        if entity_type == None:
            num_length = random.randint(1, 10) if length == None else length
            return f"{random.randint(10**(num_length-1), 10**num_length-1)}"
