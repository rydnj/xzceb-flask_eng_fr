import unittest

from machinetranslation import translator

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(translator.englishToFrench(None),None)

    def test2(self):
        self.assertEqual(translator.englishToFrench('Hello'),'Bonjour')

class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(translator.frenchToEnglish(None),None)

    def test2(self):
        self.assertEqual(translator.frenchToEnglish('Bonjour'),'Hello')

unittest.main()