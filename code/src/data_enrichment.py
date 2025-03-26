def enrich_data(entities: dict[str, list]) -> dict[str, list]:
    """Enhances extracted entities with additional metadata."""
    enriched_data = {}
    for category, values in entities.items():
        enriched_data[category] = [f"{val} (Verified)" for val in values]
    return enriched_data

if __name__ == "__main__":
    sample_entities = {"PERSON": ["Elon Musk"], "ORG": ["Tesla"]}
    print(enrich_data(sample_entities))