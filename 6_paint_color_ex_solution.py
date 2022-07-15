from collections import deque

substrings = deque(input().split())
main_colors = {'red', 'yellow', 'blue'}
secondary_colors = {'orange', 'purple', 'green'}
collected_colors = []
while substrings:
    left = substrings.popleft()
    right = substrings.pop() if substrings else ''
    color = left + right
    if color in main_colors or color in secondary_colors:
        collected_colors.append(color)
        continue
    color = right + left
    if color in main_colors or color in secondary_colors:
        collected_colors.append(color)
    else:
        left = left[:-1]
        right = right[:-1]
        if left:
            substrings.insert(len(substrings)//2, left)
        if right:
            substrings.insert(len(substrings) // 2, right)

secondary_required_colors = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}

for color in collected_colors:
    if color in main_colors:
        continue
    required_colors = secondary_required_colors[color]
    is_valid = all([x in collected_colors for x in required_colors])
    if not is_valid:
        collected_colors.remove(color)
print(collected_colors)

# another way to check the secondary colors:
#for color in collected_colors:
#    if color in main_colors:
#        continue
#    required_color1, required_color2 = secondary_required_colors[color]
#    if not (required_color1 in collected_colors) or not (required_color2 in collected_colors):
#        collected_colors.remove(color)
#print(collected_colors)