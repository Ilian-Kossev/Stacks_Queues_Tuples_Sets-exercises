from collections import deque

expression = deque(x for x in input().split())
current_expression = list()
current_expression.append(int(expression.popleft()))
result = current_expression[0]
while expression:
    num_to_add = expression.popleft()
    if num_to_add not in '/*-+':
        current_expression.append(int(num_to_add))
    else:
        operator = num_to_add
        if operator == '+':
            while len(current_expression) > 1:
                result += current_expression.pop(1)
        elif operator == '-':
            while len(current_expression) > 1:
                result -= current_expression.pop(1)
        elif operator == '*':
            while len(current_expression) > 1:
                result *= current_expression.pop(1)
        elif operator == '/':
            while len(current_expression) > 1:
                result //= current_expression.pop(1)
print(result)


