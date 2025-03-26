Project Name: RiskIntel
Table of Contents:
Introduction
Demo
Inspiration
What It Does
How We Built It
Challenges We Faced
How to Run
Tech Stack
Team

Introduction: This project focuses on entity extraction and risk analysis. It processes text to identify named entities (people, organizations, and locations) and assesses their associated risks using predefined sanction lists. The goal is to provide automated risk assessment for compliance and regulatory needs.

Inspiration: The need for automated entity recognition and risk detection in compliance, financial regulations, and cybersecurity inspired this project.

What It Does: 
1. Extracts named entities (e.g., persons, organizations, locations) from text using NLP.
2. Matches entities against a risk database to determine their risk level.
3. Outputs extracted entities and their risk classifications.

How We Built It:
1. Used spaCy for natural language processing (NLP) and entity extraction.
2. Implemented risk analysis using a predefined sanction list.
3. Developed dataset generation and testing scripts for performance evaluation.
4. Designed a structured modular architecture for easy extensibility.

Challenges We Faced:
1. Improving entity extraction accuracy.
2. Handling ambiguous text inputs.
3. Optimizing risk assessment speed for large datasets.

How to Run:
1. Clone the repository
 git clone https://github.com/your-repo.git
 cd your-repo/code
2. Install dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm
3. Generate a dataset
python dataset/dataset_generator.py 10000  # Generate 10,000 samples
4. Run the test suite
python -m test.test_dataset

Tech Stack
1. NLP: spaCy
2. Backend: Python
3. Data Processing: JSON
4. Testing: Unit tests with sample datasets
5. Team -  Savita Gupta | https://github.com/ewfx/aidel-a-g-i/tree/main/code