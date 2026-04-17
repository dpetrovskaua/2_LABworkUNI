import pytest
from main2 import TextProcessor

@pytest.fixture
def processor():
    return TextProcessor()

def test_process_basic(processor):
    assert processor.process_1word("транзистор") == "транзисор"
    assert processor.process_1word("максимум") == "максиу"
    assert processor.process_1word("minimum") == "miniu"
    assert processor.process_1word("pineapple") == "pineale"

def test_process_capital(processor):  # з великими буквами
    assert processor.process_1word("Ананас") == "Аннс"
    assert processor.process_1word("Елемент") == "Елмнт"
    assert processor.process_1word("People") == "Peole"
    assert processor.process_1word("Calculator") == "Calulator"

def test_process_small(processor):  # малі слова чи окремі букви
    assert processor.process_1word("я") == "я"
    assert processor.process_1word("її") == "ї"
    assert processor.process_1word("A") == "A"
