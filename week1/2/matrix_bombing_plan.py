from sum_matrix import sum_matrix


def matrix_bombing_plan(m):
    cordinates = {(x, y): sum_matrix(m) for x in range(3) for y in range(3)}
    return cordinates


def find_neibours(coords):
    return [(x, y) for x in [coords[0]-1, coords[0]+1] if x >= 0 and x <= 2 for y in [coords[1]-1, coords[1]+1] if y >= 0 and y <= 2]


if __name__ == '__main__':
    # print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(find_neibours((1, 2)))
