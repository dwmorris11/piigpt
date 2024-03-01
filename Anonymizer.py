import random
import os
import toml
import exrex
from Analyzers import AnalyzerType

class Anonymizer:
    def _init_(self, config_file_path = None, analyzer_type: AnalyzerType = AnalyzerType.AZURE):
        if config_file_path is None:
            file_path = os.path.join(os.path.dirname(__file__), "/Config/anonymizer_config.toml")
        self.config = None
        self.analyzer_type = analyzer_type.value
        self._load_configuration(file_path)

    def _load_configuration(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError("The anonymizer configuration file was not found")
        with open(file_path) as file:
            config = toml.load(file)
            self.config = config[self.analyzer_type]

    def anonymize(self, entity_type = None, length = None, data = None):
        if length is None and data is not None:
            length = len(data)
        if entity_type == None:
            return self.anonymize_number(None, length)
        else:
            return self.anonymize_text(entity_type, length)

    def anonymize_text(self, entity_type: str = None, length = None):
        if entity_type == None:
            text_length = random.randint(1, 10) if length == None else length
            return f"{''.join([chr(random.randint(97, 122)) for _ in range(text_length)])}"
        if entity_type in self.config\
            and "pattern" in self.config[entity_type]:
            pattern = self.config[entity_type]["pattern"]
            pattern_length = self.config[entity_type]["length"] if "length" in self.config[entity_type] else -1
            # Add length to pattern
            if length is not None:
                pattern_length = length
            if pattern_length > 0:
                pattern = f"{pattern}{{{pattern_length}}}$"
            return exrex.getone(pattern)
        elif "default" in self.config:
            pattern = self.config["default"]
            return exrex.getone(pattern)
        else:
            raise ValueError("The entity type is not supported and no default pattern is provided.")

    def anonymize_number(self, entity_type = None, length = None):
        if entity_type == None:
            num_length = random.randint(1, 10) if length == None else length
            return f"{random.randint(10**(num_length-1), 10**num_length-1)}"
