import json
import entity_extraction
import risk_analysis

def test_with_dataset():
    """Tests entity extraction and risk analysis with a large dataset."""
    try:
        with open("../dataset/sample_data.json", "r") as f:  # Adjust path if needed
            dataset = json.load(f)
        print(f"Loaded {len(dataset)} samples for testing...")

        correct_entities = 0
        correct_risk = 0
        total = len(dataset)

        for idx, entry in enumerate(dataset[:5]):  # Debug with first 5 entries
            print(f"\n[Sample {idx+1}] Text: {entry['text']}")
            extracted = entity_extraction.extract_entities(entry["text"])
            risk_result = risk_analysis.analyze_risk(extracted)

            print(f"Extracted Entities: {extracted}")
            print(f"Expected Entities: {entry['expected_entities']}")
            print(f"Risk Analysis: {risk_result}")
            print(f"Expected Risk: {entry['expected_risk']}")

            if extracted == entry["expected_entities"]:
                correct_entities += 1
            if risk_result == entry["expected_risk"]:
                correct_risk += 1

        print(f"\nEntity Extraction Accuracy: {correct_entities / total * 100:.2f}%")
        print(f"Risk Analysis Accuracy: {correct_risk / total * 100:.2f}%")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_with_dataset()
