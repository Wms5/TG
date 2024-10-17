import ast

x = r'''def bucketsort(arr, k):
    counts = [0] * k
    for x in arr:
        counts[x] += 1

    sorted_arr = []
    for i, count in enumerate(counts):
        sorted_arr.extend([i] * count)

    return sorted_arr'''

y = r'''def bucketsort(arr, k):
    counts = [0] * k
    for x in arr:
        counts[x] += 1

    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i] * counts[i])

    return sorted_arr'''

file1 = "/home/wilkinson/Documents/TCC/QuixBugs-master/python_programs/bucketsort.py"
file2 = "/home/wilkinson/Documents/TCC/QuixBugs-master/correct_python_programs/bucketsort.py"

f1 = open(file1, 'r')
f2 = open(file2, 'r')
tree1 = ast.parse(f1.read())
tree2 = ast.parse(f2.read())

xd = ast.dump(ast.parse(tree1))
yd = ast.dump(ast.parse(tree2))
print(xd == yd)
