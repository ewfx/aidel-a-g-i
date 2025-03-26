# entity_extraction.py
import spacy

def extract_entities(text):
    """Extracts named entities from text using spaCy."""
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    
    entities = {"PERSON": [], "ORG": [], "GPE": []}
    
    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].append(ent.text)
    
    # Remove duplicates
    for key in entities:
        entities[key] = list(set(entities[key]))
    
    return entities

if __name__ == "__main__":
    sample_text = "Elon Musk is the CEO of Tesla, headquartered in California."
    print("Extracted Entities:", extract_entities(sample_text))
