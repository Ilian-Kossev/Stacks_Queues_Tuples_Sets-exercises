from collections import deque


def collect_honey(arg_1, arg_2, operator):
    if operator == '-':
        return abs(arg_1 - arg_2)
    elif operator == '+':
        return abs(arg_1 + arg_2)
    elif operator == '*':
        return abs(arg_1 * arg_2)
    elif operator == '/':
        return abs(arg_1 / arg_2)


bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque([x for x in input().split()])
nectar_collected = False
total_honey = 0

while bees and nectar:
    if nectar[-1] == 0 and symbols[0] == '/':
        nectar.pop()
        bees.popleft()
        continue
    if bees[0] <= nectar[-1]:
        nectar_collected = True
    else:
        nectar.pop()
        continue
    if nectar_collected:
        total_honey += collect_honey(bees[0], nectar[-1], symbols[0])
        bees.popleft()
        nectar.pop()
        symbols.popleft()
print(f'Total honey made: {total_honey}')
if len(bees) > 0:
    print(f'Bees left: ', end='')
    print(', '.join([str(x) for x in bees]))
if len(nectar) > 0:
    print(f'Nectar left: ', end='')
    print(', '.join([str(x) for x in nectar]))




