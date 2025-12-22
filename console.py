import numpy as np

def process_output(output):
    if type(output) is int:
        if output == 0:
            print_spliter()
            print("\n\n    ==>  process stoped!\n        matrix equal zeros")
            return False

        if output == 1:
            print_spliter()
            print("\n\n    ==>  process stoped!\n        matrix of light repit")
            return False

        else:
            print_spliter()
            print("\n\n    ==>  process stoped WITH UNKNOWN ERROR!\n        UNKNOWN ERROR")
            return False
        


    return True


def print_spliter():
    n = 5
    _str = "|@@@|###|$$$|%%%|&&&"
    print("\n\n")
    for i in range(4):
        ni = i%(n+1)
        print(_str[len(_str)-ni*4: len(_str)+1], end="")

        for _ in range(8):
            print(_str, end="")

        print(_str[0: (n-(ni)) * 4])

def print_start():
    print("\n\n")
    print("    ####  PROGRAMM START  ####    \n")
    
    print("""
   |    |    |    |    |    |    |    |    |    |    |    |    |    |   
  \|/  \|/  \|/  \|/  \|/  \|/  \|/  \|/  \|/  \|/  \|/  \|/  \|/  \|/  
""")

    print("\n\n")

def print_matrix(matrix:np.ndarray, step:int=-1):
    if step >= 0:
        print("  STEP: ",step)
    
    x, y = matrix.shape
    print(f"+{"==="*y}+")
    for i in range(x):
        for line in range(2):

            print("|", end="")

            for i2 in range(y):
                if matrix[i, i2] == 1:
                    print("###", end="")
                else:
                    if line == 0:
                        print(" . ", end="")
                    else:
                        print("   ", end="")

            print("|")

    print(f"+{"==="*y}+", end="")
    print("\n\n")