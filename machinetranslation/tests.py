import translator
import unittest

class TranslatorTest(unittest.TestCase):
    def test_empty_input_frenchToEnglish(self):
        self.assertEqual(translator.frenchToEnglish(''), '')

    def test_bonjour_frenchToEnglish(self):
        self.assertEqual(translator.frenchToEnglish('Bonjour'), 'Hello')

    def test_empty_input_englishToFrench(self):
        self.assertEqual(translator.englishToFrench(''), '')

    def test_hello_englishToFrench(self):
        self.assertEqual(translator.englishToFrench('Hello'), 'Bonjour')

if __name__ == '__main__':
    unittest.main()