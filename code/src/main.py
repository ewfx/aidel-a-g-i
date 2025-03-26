import entity_extraction
import risk_analysis
import data_enrichment

def main():
    """Main function to run entity extraction, enrichment, and risk analysis."""
    text = "Elon Musk is the CEO of Tesla, headquartered in California."
    entities = entity_extraction.extract_entities(text)
    enriched_entities = data_enrichment.enrich_data(entities)
    risk_report = risk_analysis.analyze_risk(enriched_entities)
    
    print("Extracted Entities:")
    print(enriched_entities)
    print("\nRisk Analysis:")
    print(risk_report)

if __name__ == "__main__":
    main()