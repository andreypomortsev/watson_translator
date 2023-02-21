import translator
import unittest

class French(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(translator.frenchToEnglish(''), '')
        self.assertEqual(translator.frenchToEnglish('Bonjour'), 'Hello')

    def test_englishToFrench(self):
        self.assertEqual(translator.englishToFrench(''), '')
        self.assertEqual(translator.englishToFrench('Hello'), 'Bonjour')