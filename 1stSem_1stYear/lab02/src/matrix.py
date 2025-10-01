def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat)==0:
        return []
    rowlenght=len(mat[0])
    for row in mat:
        if len(row)!=rowlenght:
            return ValueError
    return [[row[index] for row in mat] for index in range(rowlenght)]

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat)==0:
        return []
    rowlenght=len(mat[0])
    for row in mat:
        if len(row)!=rowlenght:
            return ValueError
    return [sum(row) for row in mat]

def col_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat)==0:
        return []
    rowlenght=len(mat[0])
    for row in mat:
        if len(row)!=rowlenght:
            return ValueError
    newmat=transpose(mat)
    return [sum(row) for row in newmat]
