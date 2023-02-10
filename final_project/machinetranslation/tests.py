import unittest

from translator import french_to_english, english_to_french

class TestLanguage(unittest.TestCase):
    """ Hopefully this code works """
    def test(self):
        self.assertEqual(french_to_english("Au Revoir"), "Goodbye")
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("Goodbye"), "Au Revoir")

unittest.main()
