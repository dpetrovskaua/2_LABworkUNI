import unittest
from main2 import TextProcessor

class TestTextProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = TextProcessor()

    def test_process_basic(self):
        self.assertEqual(self.processor.process_1word("транзистор"), "транзисор")
        self.assertEqual(self.processor.process_1word("максимум"), "максиу")
        self.assertEqual(self.processor.process_1word("minimum"), "miniu")
        self.assertEqual(self.processor.process_1word("pineapple"), "pineale")
    
    def test_process_capital(self): # з великими буквами
        self.assertEqual(self.processor.process_1word("Ананас"), "Аннс")
        self.assertEqual(self.processor.process_1word("Елемент"), "Елмнт")
        self.assertEqual(self.processor.process_1word("People"), "Peole")
        self.assertEqual(self.processor.process_1word("Calculator"), "Calulator")

    def test_process_small(self): # малі слова чи окремі букви
        self.assertEqual(self.processor.process_1word("я"), "я")
        self.assertEqual(self.processor.process_1word("її"), "ї")
         self.assertEqual(self.processor.process_1word("A"), "A")
        
if __name__ == "__main__":
    unittest.main()
