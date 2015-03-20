def group(items):
    groups = []
    current_item = items[0]
    current_group = []
    for i in items:
        if i == current_item:
            current_group.append(i)
        else:
            current_item = i
            groups.append(current_group)
            current_group = []
            current_group.append(i)
    groups.append(current_group)
    return groups


if __name__ == '__main__':
    print(group([1, 1, 1, 2, 3, 1, 1]))
    print(group([1, 2, 1, 2, 3, 3]))
