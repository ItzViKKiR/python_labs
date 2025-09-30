# Лабораторная работа 1
### Задание 1
```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int, ValueError]:
    if len(nums)==0:
        return ValueError
    else:
        return min(nums), max(nums)

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

def flatten(mat: list[list | tuple]) -> list | type[TypeError]:
    result=[]
    for object in mat:
        if type(object) is not list or not tuple:
            return TypeError
        else:
            for item in object:
                result.append(item)
    return result
```
![arrays code](/images/lab02/arrays.png)



