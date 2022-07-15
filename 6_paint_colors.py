from collections import deque


def delete_last_chr_in_first_position(collection: deque):
    if len(collection[0]) == 1:
        collection.popleft()
        return
    else:
        altered_seq = collection.popleft()[0:-1]
        return altered_seq


def delete_last_chr_in_last_position(collection: deque):
    if len(collection[-1]) == 1:
        collection.pop()
    else:
        altered_seq = collection.pop()[0:-1]
        return altered_seq


#def check_color(first_str: str, second_str: str):
#    color_collection = ['red', 'blue', 'yellow', 'orange', 'purple', 'green']
#    first_check = first_str + second_str
#    second_check = second_str + first_str
#    if first_check in color_collection:
#        searched_color = first_check
#    elif second_check in color_collection:
#        searched_color = second_check
 #   else:
#        searched_color = first_check
 #       return searched_color


string = deque(input().split())
colors_found = []
color_list = ['red', 'blue', 'yellow', 'orange', 'purple', 'green']
while string:
    if len(string) > 1:
        color = string[0] + string[-1]
        if color in color_list:
            colors_found.append(color)
            string.popleft()
            string.pop()
            continue
        else:
            color = string[-1] + string[0]
            if color in color_list:
                colors_found.append(color)
                string.popleft()
                string.pop()
                continue
    else:
        color = string[0]
        if len(color) < 3:
            break
        else:
            if color in color_list:
                colors_found.append(color)
                string.popleft()
                continue
    changed_first_string = delete_last_chr_in_first_position(string)
    if not string:
        break
    changed_last_string = delete_last_chr_in_last_position(string)
    insert_index = len(string) // 2
    string.insert(insert_index, changed_first_string)
    string.insert(insert_index, changed_last_string)
    if changed_last_string or changed_first_string is None:
        string = deque([x for x in string if x is not None])
if 'orange' in colors_found:
    if 'red' and 'yellow' not in colors_found:
        colors_found.remove('orange')
if 'purple' in colors_found:
    if 'red' and 'blue' not in colors_found:
        colors_found.remove('purple')
if 'green' in colors_found:
    if 'yellow' and 'blue' not in colors_found:
        colors_found.remove('yellow')

print(colors_found)
#judge = 90/100


