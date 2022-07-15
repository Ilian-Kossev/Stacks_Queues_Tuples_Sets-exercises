from collections import deque

from math import floor

expression_list = deque(input().split(' '))
operations_list = []
result = int(expression_list[0])
expression_list.popleft()
while expression_list:
    operations_list.append(expression_list.popleft())
    if operations_list[-1] == '-':
        operations_list.pop()
        operations_list.insert(0, result)
        for num in range(1, len(operations_list)):
            result -= int(operations_list[num])
        operations_list.clear()
    elif operations_list[-1] == '+':
        operations_list.pop()
        operations_list.insert(0, result)
        for num in range(1, len(operations_list)):
            result += int(operations_list[num])
        operations_list.clear()
    elif operations_list[-1] == '/':
        operations_list.pop()
        operations_list.insert(0, result)
        for num in range(1, len(operations_list)):
            result /= (int(operations_list[num]))
            result = floor(result)
        operations_list.clear()
    elif operations_list[-1] == '*':
        operations_list.pop()
        operations_list.insert(0, result)
        for num in range(1, len(operations_list)):
            result *= int(operations_list[num])
        operations_list.clear()

print(result)


