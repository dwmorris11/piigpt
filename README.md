# piigpt

Provides a mechanism to anonymize PII and PHI before sending to a LLM API

## Basic Setup:

```
from Analyzers.AnalyzerType import AnalyzerType
from PIIScrubber import PIIScrubber

def main():
    from dotenv import load_dotenv
    load_dotenv("sample.env")
    pii = PIIScrubber(AnalyzerType.AZURE)
    text = "My phone number is 555-555-5555"
    print(pii.scrub([text]))
    print(pii.get_entities([text]))
    print(pii.anonymize(pii.get_entities([text]), text))
    print(pii.deanonymize(pii.anonymize(pii.get_entities([text]), text)))

if __name__ == "__main__":
    main()
```

**Output:**
['My phone number is ************']
[Text: 555-555-5555, Category: PhoneNumber, Subcategory: None, Offset: 19, Length: 12]
My phone number is :yudDNDuGJG:
My phone number is 555-555-5555

## Extensible
#### Analyzers:
Currently AzureAIAnalyzer is supported.  Contribute by adding additional analyzers following the BaseAnalyzer interface.
Configure your parameters for your analyzer in the analyzer_config.toml file

#### Anonymizers:
Plug in your own anonymizer or use the built in Anonymizer.
Change how the built in anonymizer anonymizes entities by changing the anonymizer_config.toml file or use the defaults.

### CacheProviders:
Use the built in dictionary cache provider or insert your own CacheProvider following the BaseCache interface.
Cache ensures all PII is deleted in a timely manner

