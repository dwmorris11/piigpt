from Analyzers.AnalyzerType import AnalyzerType
from PIIScrubber import PIIScrubber

def main():
    from dotenv import load_dotenv
    load_dotenv("test.env")
    pii = PIIScrubber(AnalyzerType.AZURE)
    text = "Bob is a man.  Bob is 30 years old.  Bob is a doctor."
    print(pii.scrub([text]))
    print(pii.get_entities([text]))
    print(pii.anonymize(pii.get_entities([text]), text))
    print(pii.deanonymize(pii.anonymize(pii.get_entities([text]), text)))
    print(pii.anonymize_maintain_context(pii.get_entities([text]), text))
    print(pii.deanonymize(pii.anonymize(pii.get_entities([text]), text)))

if __name__ == "__main__":
    main()