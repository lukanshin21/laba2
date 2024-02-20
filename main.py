def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]


def bubble_sort(num):
    sort_num = num.copy()
    n = len(sort_num)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if sort_num[j] > sort_num[j + 1]:
                sort_num[j], sort_num[j + 1] = sort_num[j + 1], sort_num[j]
    return sort_num


def calc(num1, num2, operation):
    if operation == "+":
        answer = num1 + num2
        return answer
    elif operation == "-":
        answer = num1 - num2
        return answer
    elif operation == "*":
        answer = num1 * num2
        return answer
    elif operation == "/":
        if num2 != 0:
            answer = num1 / num2
            return answer
        else:
            return "Деление на ноль"
    else:
        return "Задана неизвестная операция"
