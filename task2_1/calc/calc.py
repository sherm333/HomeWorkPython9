# Разбитие строки на операнды и операторы.
def expression_splitter(math_expression: str):
    math_expression = math_expression.replace(',', '.')
    for value in math_expression:
        if value in '+-*/()=':
            math_expression = math_expression.replace(f'{value}', f' {value} ')
    math_expression = math_expression.split()
    while '=' in math_expression:
        math_expression.pop()
    return math_expression


# Создание нотации из списка.
def reverse_polish_notation_maker(math_expression: list):
    priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
    rstack, stack = [], []
    for value in math_expression:
        if value in '(':
            stack.append(value)
        elif value in ')':
            while stack[-1] != '(':
                rstack.append(stack.pop())
            stack.pop()
        elif value in '+-*/':
            if len(stack) == 0 or priority[stack[-1]] < priority[value]:
                stack.append(value)
            elif priority[stack[-1]] >= priority[value]:
                rstack.append(stack.pop())
                stack.append(value)
        else:
            rstack.append(float(value))
    rstack.extend(stack[::-1])
    return rstack


# Операции над числами.
def operationist(x, y, key):
    operations = {'+': lambda x, y: x + y,
                  '-': lambda x, y: x - y,
                  '*': lambda x, y: x * y,
                  '/': lambda x, y: x / y}
    return operations[key](x, y)


# Калькуляция результата выражения.
def expression_calculator(math_expression: list):
    result = []
    for value in math_expression:
        if str(value) in '+-*/':
            x, y = result.pop(), result.pop()
            result.append(operationist(y, x, value))
        else:
            result.append(value)
    return result[0]


# Вызываемый ботом метод.
def calculator(message):
    math_expression = str(message)
    math_expression = expression_calculator(
        reverse_polish_notation_maker(expression_splitter(math_expression)))
    if float(math_expression) - int(math_expression) > 0:
        return math_expression
    else:
        return int(math_expression)