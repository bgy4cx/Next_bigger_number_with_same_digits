from main import next_bigger

def test_next_bigger_1():
    assert next_bigger(12) == 21

def test_next_bigger_2():
    assert next_bigger(513) == 531

def test_next_bigger_3():
    assert next_bigger(2017) == 2071

def test_next_bigger_4():
    assert next_bigger(414) == 441

def test_next_bigger_5():
    assert next_bigger(144) == 414

def test_next_bigger_6():
    assert next_bigger(1234567908) == 1234567980

def test_next_bigger_7():
    assert next_bigger(111) == -1

def test_next_bigger_8():
    assert next_bigger(1234567890) == 1234567908

def test_next_bigger_9():
    assert next_bigger(59884848459853) == 59884848483559