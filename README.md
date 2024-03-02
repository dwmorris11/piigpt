# piigpt

Provides a mechanism to anonymize PII and PHI before sending to a LLM API.

Using the anonymize function will generate a different anonymous symbol for each entity.

Using the anonymize_maintain_context function uses the same anonymous symbol for every occurrence of the same word.

## Basic Setup:

```
from Analyzers.AnalyzerType import AnalyzerType
from PIIScrubber import PIIScrubber

def main():
    from dotenv import load_dotenv
    load_dotenv("sample.env")
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
```

**Output:**
['*** is a man.  *** is ************.  *** is a ******.']
[Text: Bob, Category: Person, Subcategory: None, Offset: 0, Length: 3, Text: Bob, Category: Person, Subcategory: None, Offset: 15, Length: 3, Text: 30 years old, Category: Quantity, Subcategory: Age, Offset: 22, Length: 12, Text: Bob, Category: Person, Subcategory: None, Offset: 37, Length: 3, Text: doctor, Category: PersonType, Subcategory: None, Offset: 46, Length: 6]
:GusUWBK7aC: is a man.  :GusUWBK7aC: is :YgmVZxmRW6:.  :GusUWBK7aC: is a :QKFaqn1HRv:.
Bob is a man.  Bob is 30 years old.  Bob is a doctor.
:TSEuDSIxsw: is a man.  :TSEuDSIxsw: is :bl8EurovmC:.  :TSEuDSIxsw: is a :9pMYbEhLwd:.
Bob is a man.  Bob is 30 years old.  Bob is a doctor.

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

