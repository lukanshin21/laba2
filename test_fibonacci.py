from main import fibonacci

# Проверка вывода трех чисел фибоначчи
def test_fibonacci_1():
    assert fibonacci(3) == [0, 1, 1]

# Проверка вывода 10 чисел фибоначчи
def test_fibonacci_2():
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Негативная проверка вывода 10 чисел фибоначчи
def test_fibonacci_3():
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 10, 21, 34]

# Проверка вывода 9 чисел фибоначчи
def test_fibonacci_4():
    assert fibonacci(9) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
