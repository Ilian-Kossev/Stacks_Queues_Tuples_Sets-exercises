from collections import deque

chocolates = [int(x) for x in input().split(', ')]
milk = deque([int(x) for x in input().split(', ')])
counter_shakes = 0
five_shakes_made = False
while chocolates and milk:
    if chocolates[-1] <= 0 and milk[0] <= 0:
        chocolates.pop()
        milk.popleft()
        continue
    else:
        if chocolates[-1] <= 0:
            chocolates.pop()
            continue
        elif milk[0] <= 0:
            milk.popleft()
            continue
    if chocolates[-1] == milk[0]:
        counter_shakes += 1
        chocolates.pop()
        milk.popleft()
        if counter_shakes == 5:
            five_shakes_made = True
            break
    else:
        chocolates[-1] -= 5
        milk.rotate(-1)
if five_shakes_made:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')
if len(chocolates) > 0:
    print(f'Chocolate: ', end='')
    print(', '.join([str(x) for x in chocolates]))
else:
    print('Chocolate: empty')
if len(milk) > 0:
    print(f'Milk: ', end='')
    print(', '.join([str(x) for x in milk]))
else:
    print('Milk: empty')
