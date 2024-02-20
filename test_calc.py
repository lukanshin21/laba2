from main import calc


# Проверка функции сложения
def test_sum():
    assert calc(3, 2, "+") == 5


# Проверка функции вычитания
def test_substract():
    assert calc(3, 2, "-") == 1


# Проверка функции умножения
def test_multiply():
    assert calc(3, 2, "*") == 8


# Проверка функции деления
def test_divide():
    assert calc(3, 2, "/") == 1.5


# Проверка вывода текста с ошибкой при делении на ноль
def test_divide_zero():
    assert calc(3, 0, "/") == 0


def test_unknown():
    assert calc(3, 2, "*/") == "Задана неизвестная операция"
