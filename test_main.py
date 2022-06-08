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
    assert next_bigger(144) == 144

