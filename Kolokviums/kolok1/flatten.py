flatten = [[1, 2, [3, 4]], [5, 6, 6], 9]

def flatten_list(el):
    empty_list = []
    for i in el:
        if isinstance(i, list):
            empty_list += flatten_list(i)
        else:
            empty_list.append(i)
    return empty_list

print(flatten_list(flatten))