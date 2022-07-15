from collections import deque

collection = {
    'Doll': 150,
    'Wooden train': 250,
    'Teddy bear': 300,
    'Bicycle': 400
}
present_made = {}
task_fulfilled = False
materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])
while materials and magic_level:
    present_crafted = False
    result = materials[-1] * magic_level[0]
    for key, value in collection.items():
        if result == value:
            if key not in present_made:
                present_made[key] = 0
            present_made[key] += 1
            present_crafted = True
            materials.pop()
            magic_level.popleft()
            break
    if present_crafted:
        continue
    else:
        if result < 0:
            new_result = materials.pop() + magic_level.popleft()
            materials.append(new_result)
        elif result > 0:
            magic_level.popleft()
            materials[-1] += 15
        else:
            if materials[-1] == 0 and magic_level[0] == 0:
                materials.pop()
                magic_level.popleft()
                continue
            elif materials[-1] == 0:
                materials.pop()
                continue
            elif magic_level[0] == 0:
                magic_level.popleft()
                continue
if 'Doll' and 'Wooden train' in present_made:
    task_fulfilled = True
elif 'Teddy bear' and 'Bicycle' in present_made:
    task_fulfilled = True
if task_fulfilled:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')
if len(materials) > 0:
    print('Materials left: ', end='')
    print(', '.join([str(x) for x in materials[::-1]]))
if len(magic_level) > 0:
    print('Magic left: ', end='')
    print(', '.join([str(x) for x in magic_level[::-1]]))
sorted_presents = dict(sorted(present_made.items(), key=lambda x: x[0]))
for key, value in sorted_presents.items():
    if sorted_presents[key] > 0:
        print(f'{key}: {value}')






