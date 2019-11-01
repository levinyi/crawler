import numpy as np


def read_file(path):
    f = open(path)
    first_ele = True
    for data in f.readlines():
        data = data.rstrip("\n")
        nums = data.split()
        if first_ele:
            nums = [int(x) for x in nums]
            matrix = np.array(nums)
            first_ele = False
        else:
            nums = [int(x) for x in nums]
            matrix = np.c_[matrix, nums]
    deal_matrix(matrix)
    f.close()


def deal_matrix(matrix):
    print("transpose the matrix")
    matrix = matrix.transpose()
    print(matrix)
    print("matrix trace")
    print(np.trace(matrix))


def fixed_matrix(row, col):
    return [[0 for i in range(col)] for j in range(row)]


if __name__ == '__main__':
    read_file("matrix")