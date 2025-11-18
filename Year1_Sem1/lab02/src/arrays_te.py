import arrays

print("min_max ")
print("[3, -1, 5, 5, 0] ->", arrays.min_max([3, -1, 5, 5, 0]))
print("[42] ->", arrays.min_max([42]))
print("[-5, -2 ,-9] ->", arrays.min_max([-5, -2, -9]))
print("[] ->", arrays.min_max([]))
print("[1.5, 2, 2.0, -3.1] ->", arrays.min_max([1.5, 2, 2.0, -3.1]))

print("unique_sorted")
print("[3, 1, 2, 1, 3] ->", arrays.unique_sorted([3, 1, 2, 1, 3]))
print("[] ->", arrays.unique_sorted([]))
print("[-1, -1, 0, 2, 2] ->", arrays.unique_sorted([-1, -1, 0, 2, 2]))
print("[1.0, 1, 2.5, 2.5, 0] ->", arrays.unique_sorted([1.0, 1, 2.5, 2.5, 0]))

print("flatten function")
print("[[1, 2], [3, 4]] ->", arrays.flatten([[1, 2], [3, 4]]))
print("[[1, 2], (3, 4, 5)] ->", arrays.flatten([[1, 2], (3, 4, 5)]))
print("[[1], [], [2, 3]] ->", arrays.flatten([[1], [], [2, 3]]))
print(f"[[1, 2], 'ab'] ->", arrays.flatten([[1, 2], "ab"]))  # type: ignore
