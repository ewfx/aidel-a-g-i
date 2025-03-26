import unittest
from src.entity_extraction import extract_entities

class TestEntityExtractor(unittest.TestCase):
    def test_extract_entities(self):
        text = "Barack Obama was born in Hawaii."
        entities = extract_entities(text)
        self.assertIn("PERSON", entities)
        self.assertIn("Barack Obama", entities["PERSON"])

if __name__ == '__main__':
    unittest.main()