from collections import deque

present_made = {
        'Doll': 0,
        'Wooden train': 0,
        'Teddy bear': 0,
        'Bicycle': 0
}
materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])
task_fulfilled = False
while materials and magic_level:
    arg_1 = materials[-1]
    arg_2 = magic_level[0]
    result = arg_1 * arg_2
    if result == 150:
        present_made['Doll'] += 1
        materials.pop()
        magic_level.popleft()
    elif result == 250:
        present_made['Wooden train'] += 1
        materials.pop()
        magic_level.popleft()
    elif result == 300:
        present_made['Teddy bear'] += 1
        materials.pop()
        magic_level.popleft()
    elif result == 400:
        present_made['Bicycle'] += 1
        materials.pop()
        magic_level.popleft()
    else:
        if result < 0:
            result = arg_1 + arg_2
            materials.pop()
            magic_level.popleft()
            materials.append(result)
        elif result > 0:
            magic_level.popleft()
            materials[-1] += 15
        elif materials[-1] == 0:
            materials.pop()
        elif magic_level[0] == 0:
            magic_level.popleft()

if present_made['Doll'] > 0 and present_made['Wooden train'] > 0:
    task_fulfilled = True
elif present_made['Teddy bear'] > 0 and present_made['Bicycle'] > 0:
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
# judge: 80/100