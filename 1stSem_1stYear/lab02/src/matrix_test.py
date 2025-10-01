from matrix import*
print('transpose')
print("[[1, 2, 3]] ->", transpose([[1, 2, 3]]))
print("[[1], [2], [3]] ->", transpose([[1], [2], [3]]))
print("[[1, 2], [3, 4]] ->", transpose([[1, 2], [3, 4]]))
print("[] ->", transpose([]))
print("[[1, 2], [3]] ->", transpose([[1, 2], [3]]))

print('row_sums')
print('[[1, 2, 3], [4, 5, 6]] ->', row_sums([[1, 2, 3], [4, 5, 6]]))
print('[[-1, 1], [10, -10]] ->', row_sums([[-1, 1], [10, -10]]))
print('[[0, 0], [0, 0]] ->', row_sums([[0, 0], [0, 0]]))
print('[[1, 2], [3]] ->', row_sums([[1, 2], [3]]))

print('col_sums')
print('[[1, 2, 3], [4, 5, 6]] ->', col_sums([[1, 2, 3], [4, 5, 6]]))
print('[[-1, 1], [10, -10]] ->', col_sums([[-1, 1], [10, -10]]))
print('[[0, 0], [0, 0]] ->', col_sums([[0, 0], [0, 0]]))
print('[[1, 2], [3]] ->', col_sums([[1, 2], [3]]))