# Лабораторная работа 2
### Задание 1
```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums)==0:
        raise ValueError
    else:
        return min(nums), max(nums)

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

def flatten(mat: list[list | tuple]) -> list:
    result=[]
    for object in mat:
        if type(object) is not list or not tuple:
            raise TypeError
        else:
            for item in object:
                result.append(item)
    return result
```
![arrays code](/1stSem_1stYear/lab02/images/arrays.png)

### Задание 2
``` python
def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat)==0:
        return []
    rowlenght=len(mat[0])
    for row in mat:
        if len(row)!=rowlenght:
            raise ValueError
    return [[row[index] for row in mat] for index in range(rowlenght)]

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat)==0:
        return []
    rowlenght=len(mat[0])
    for row in mat:
        if len(row)!=rowlenght:
            raise ValueError
    return [sum(row) for row in mat]

def col_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat)==0:
        return []
    rowlenght=len(mat[0])
    for row in mat:
        if len(row)!=rowlenght:
            raise ValueError
    newmat=transpose(mat)
    return [sum(row) for row in newmat]
```
![matrix code](/1stSem_1stYear/lab02/images/matrix.png)

### Задание 3
```python
def format_record(rec: tuple[str, str, float]) -> str:
    if type(rec[2]) is not int and type(rec[2]) is not float:
        raise TypeError
    if len(rec[1])==0:
        raise ValueError
    name_parts=rec[0].strip().split()
    if len(name_parts)==3:
        n1, n2, n3 = name_parts
        return f"{n1.capitalize()} {n2[0].upper()}.{n3[0].upper()}., гр. {rec[1].upper()}, GPA {rec[2]:.2f}"
    elif len(name_parts)==2:
        n1, n2 = name_parts
        return f"{n1.capitalize()} {n2[0].upper()}., гр. {rec[1].upper()}, GPA {rec[2]:.2f}"
    else:
        raise ValueError
```
![tuples code](/1stSem_1stYear/lab02/images/tuples.png)