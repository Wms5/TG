import ast
import sys
import os

def compare_python_files(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            tree1 = ast.parse(f1.read())
            tree2 = ast.parse(f2.read())
        return ast.dump(tree1) == ast.dump(tree2)
    except Exception as e:
        print(f"Error to compare the files: {e}")
        return False

algorithm = sys.argv[1]
file1 = os.getcwd() + "/QuixBugs/correct_python_programs/" + algorithm + ".py"
file2 = os.getcwd() + "/QuixBugs/python_programs/" + algorithm + ".py"

if compare_python_files(file1, file2):
    print("Same AST")
else:
    print("Different AST")
