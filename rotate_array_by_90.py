def rotate_90(game):
    row_length = n
    column_length = n

    res = [[0] * n for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length - 1 - r] = game[r][c]

    return res