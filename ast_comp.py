import ast

def compare_python_files(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            print(f1)
            print(f2)
            tree1 = ast.parse(f1.read())
            tree2 = ast.parse(f2.read())
            print(tree1)
            print(tree2)
        return ast.dump(tree1) == ast.dump(tree2)
    except Exception as e:
        print(f"Erro ao comparar arquivos: {e}")
        return False

file1 = "/home/wilkinson/Documents/TCC/QuixBugs-master/python_programs/bucketsort.py"
#file2 = "/home/wilkinson/Documents/TCC/QuixBugs-master/correct_python_programs/bucketsort.py"
file2 = "/home/wilkinson/Documents/TCC/QuixBugs-master/python_programs/bucketsort.py"
if compare_python_files(file1, file2):
    print("mesma arvore sintatica.")
else:
    print("arvores sintaticas diferentes.")
