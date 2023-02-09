import unittest

from translator.py imoprt frenchToEnglish, englishToFrench

class TestLanguage(unittest.TestCase):
  def test(self):
    self.assertEqual(frenchToEnglish("Au Revoir"), "Goodbye")
    self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
    self.assertEqual(englishToFrench("Hello"), "Bonjour")
    self.assertEqual(englishToFrench("Goodbye"), "Au Revoir")

unittest.main()
