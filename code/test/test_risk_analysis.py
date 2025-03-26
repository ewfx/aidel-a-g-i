import unittest
from src.risk_analysis import analyze_risk

class TestRiskAnalyzer(unittest.TestCase):
    def test_check_sanctions(self):
        entities = {"PERSON": ["Elon Musk"], "ORG": ["Tesla"]}
        result = analyze_risk(entities)
        self.assertIsInstance(result, dict)

if __name__ == '__main__':
    unittest.main()