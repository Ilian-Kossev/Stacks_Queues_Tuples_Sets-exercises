def check_subset(set1, set2):
    if set1 < set2:
        print(True)
    elif set2 < set1:
        print(True)
    else:
        print(False)


set_1 = {int(x) for x in input().split()}
set_2 = {int(x) for x in input().split()}
n = int(input())
for _ in range(n):
    command = input()
    if command.startswith('Add First'):
        set_to_add = {int(x) for x in command.split()[2:]}
        set_1 = set_1 | set_to_add
    elif command.startswith('Add Second'):
        set_to_add = {int(x) for x in command.split()[2:]}
        set_2 = set_2 | set_to_add
    elif command.startswith('Remove First'):
        set_to_remove = {int(x) for x in command.split()[2:]}
        set_1 = set_1 - set_to_remove
    elif command.startswith('Remove Second'):
        set_to_remove = {int(x) for x in command.split()[2:]}
        set_2 = set_2 - set_to_remove
    elif command.startswith('Check Subset'):
        check_subset(set_1, set_2)
print(', '.join(str(x) for x in sorted(set_1)))
print(', '.join(str(x) for x in sorted(set_2)))

