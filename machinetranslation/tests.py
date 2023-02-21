import unittest
import translator


class TranslatorTest(unittest.TestCase):
    """Test translator.py with empty str, and 'Hello'"""
    
    def test_empty_input_french_to_english(self):
        """Test frenchToEnglish with an empty input"""
        self.assertEqual(translator.frenchToEnglish(''), '')

    def test_bonjour_french_to_english(self):
        """Test frenchToEnglish with 'Bonjour' as the input"""
        self.assertEqual(translator.frenchToEnglish('Bonjour'), 'Hello')

    def test_empty_input_english_to_french(self):
        """Test englishToFrench with an empty input"""
        self.assertEqual(translator.englishToFrench(''), '')

    def test_hello_english_to_french(self):
        """Test englishToFrench with 'Hello' as the input"""
        self.assertEqual(translator.englishToFrench('Hello'), 'Bonjour')

if __name__ == '__main__':
    unittest.main()
