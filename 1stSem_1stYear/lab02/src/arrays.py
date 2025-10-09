def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums)==0:
        raise ValueError('Пустая матрица')
    else:
        return min(nums), max(nums)

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

def flatten(mat: list[list | tuple]) -> list:
    result=[]
    for object in mat:
        if type(object) is not list or not tuple:
            raise TypeError("Элемент не является списком/кортежем")
        else:
            for item in object:
                result.append(item)
    return result
    