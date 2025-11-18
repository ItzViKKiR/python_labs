def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat) == 0:
        return []
    rowlenght = len(mat[0])
    for row in mat:
        if len(row) != rowlenght:
            raise ValueError("Рваная матрица")
    return [[row[index] for row in mat] for index in range(rowlenght)]


def row_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat) == 0:
        return []
    rowlenght = len(mat[0])
    for row in mat:
        if len(row) != rowlenght:
            raise ValueError("Рваная матрица")
    return [sum(row) for row in mat]


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat) == 0:
        return []
    rowlenght = len(mat[0])
    for row in mat:
        if len(row) != rowlenght:
            raise ValueError("Рваная матрица")
    newmat = transpose(mat)
    return [sum(row) for row in newmat]
