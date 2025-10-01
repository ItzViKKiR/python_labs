def transpose(mat: list[list[float | int]]) -> list[list | ValueError]:
    if len(mat)==0:
        return []
    rowlenght=len(mat[0])
    for row in mat:
        if len(row)!=rowlenght:
            return ValueError
    return [[row[i] for row in mat] for i in range(rowlenght)]

def row_sums(mat: list[list[float | int]]) -> list[float] | ValueError:
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
