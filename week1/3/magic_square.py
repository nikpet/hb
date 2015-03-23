def magic_square(matrix):
    sums_of_rows = [sum(x) for x in matrix]
    sums_of_cols = [sum(x) for x in zip(*matrix)]
    diag1 = sum([matrix[x][x] for x in range(len(matrix))])
    diag2 = sum([matrix[x][len(matrix) - x - 1] for x in range(len(matrix))])
    return len(set(sums_of_rows) | set(sums_of_cols) | set([diag1]) | set([diag2])) == 1



if __name__ == '__main__':
    print(magic_square([[1,2,3], [4,5,6], [7,8,9]]))
    print(magic_square([[4,9,2], [3,5,7], [8,1,6]]))
    print(magic_square([[7,12,1,14], [2,13,8,11], [16,3,10,5], [9,6,15,4]]))
    print(magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
    print(magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))
