from Analyzers import AnalyzerType
from PIIScrubber import PIIScrubber

def main():
    pii = PIIScrubber(AnalyzerType.AZURE)
    text = "My phone number is 555-555-5555"
    print(pii.scrub([text]))