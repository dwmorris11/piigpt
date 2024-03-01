from Analyzers.AnalyzerType import AnalyzerType
from PIIScrubber import PIIScrubber

def main():
    from dotenv import load_dotenv
    load_dotenv("sample.env")
    pii = PIIScrubber(AnalyzerType.AZURE)
    text = "My phone number is 555-555-5555"
    print(pii.scrub([text]))

if __name__ == "__main__":
    main()