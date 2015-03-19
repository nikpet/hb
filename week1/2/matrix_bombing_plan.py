from sum_matrix import sum_matrix


def matrix_bombing_plan(m):
    coords = [(x, y) for x in range(3) for y in range(3)]
    bombed = {}
    for cor in coords:
        matrix_to_bomb = [[x for x in y] for y in m]
        bombed[cor] = sum_matrix(negative_to_zero(bomb(matrix_to_bomb, cor)))
    return bombed


def bomb(m, coords):
    damage = m[coords[0]][coords[1]]
    for x, y in find_neibours(coords):
        m[x][y] -= damage
    return m


def negative_to_zero(m):
    return [[y if y > 0 else 0 for y in x] for x in m]
    # return [[max(0, y) for y in x] for x in m]


def find_neibours(coords):
    neibours = [(x, y)
                for x in range(coords[0]-1, coords[0]+2)
                if x >= 0 and x <= 2
                for y in range(coords[1]-1, coords[1]+2)
                if y >= 0 and y <= 2]
    neibours.remove(coords)
    return neibours


if __name__ == '__main__':
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrix_bombing_plan(m))
    # print(sum_matrix(negative_to_zero(bomb(m, (2,2)))))
    # print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
