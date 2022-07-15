from collections import deque


def craft_present(arg_1: int, arg_2: int, collection: dict, collection_1: list, collection_2: deque):
    collection = {
        'Doll': 0,
        'Wooden train': 0,
        'Teddy bear': 0,
        'Bicycle': 0
    }
    result = arg_1 * arg_2
    collection_2 = deque()
    if result == 150:
        collection['Doll'] += 1
        collection_1.pop()
        collection_2.popleft()
    elif result == 250:
        collection['Wooden train'] += 1
        collection_1.pop()
        collection_2.popleft()
    elif result == 300:
        collection['Teddy bear'] += 1
        collection_1.pop()
        collection_2.popleft()
    elif result == 400:
        collection['Bicycle'] += 1
        collection_1.pop()
        collection_2.popleft()
    else:
        if result < 0:
            result = arg_1 + arg_2
            collection_1.pop()
            collection_2.popleft()
            collection_1.append(result)
        elif result > 0:
            collection_2.popleft()
            collection_1[-1] += 15
        elif collection_1[-1] == 0:
            collection_1.pop()
        elif collection_2[0] == 0:
            collection_2.popleft()


present_made = {}
materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])
task_fulfilled = False
while materials and magic_level:
    craft_present(materials[-1], magic_level[0], present_made, materials, magic_level)
    if present_made['Doll'] > 0 and present_made['Wooden train'] > 0:
        task_fulfilled = True
    elif present_made['Teddy bear'] > 0 and present_made['Bicycle'] > 0:
        task_fulfilled = True
if task_fulfilled:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')
if len(materials) > 0:
    print('Material left: ', end='')
    print(', '.join([str(x) for x in materials]))
if len(magic_level) > 0:
    print('Magic left: ', end='')
    print(', '.join([str(x) for x in magic_level]))
for key, value in present_made.items():
    if present_made[key] > 0:
        print(f'{key}: {value}')


