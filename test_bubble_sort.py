from main import bubble_sort


# Проверка на пустой список
def test_bubble_sort_empty():
    assert bubble_sort([]) == []


# Проверка на список из одного элемента
def test_bubble_sort_single():
    assert bubble_sort([1]) == [1]


# Проверка на список из повторяющихся элементов
def test_bubble_sort_repeat():
    assert bubble_sort([5, 1, 2, 5, 2]) == [1, 2, 2, 5, 5]


# Проверка на список с отрицательными элементами
def test_bubble_sort_negative():
    assert bubble_sort([2, -2, 4, 0, -3]) == [0, 2, -2, -3, 4]
