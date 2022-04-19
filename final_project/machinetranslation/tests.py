import unittest
from translator import englishToFrench
from translator import frenchToEnglish

class test(unittest.TestCase):
    def e2f(self):
        self.assertNotEqual(englishToFrench("None"), '')
        self.assertNotEqual(englishToFrench(0), 0)
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

class test1(unittest.TestCase):
    def f2e(self):
        self.assertNotEqual(frenchToEnglish("None"), '')
        self.assertNotEqual(frenchToEnglish(0), 0)
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

unittest.main()        