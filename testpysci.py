import os
import scipy.io
matrix_dir = "G:\projects\R_stuff"
mat = scipy.io.mmread(os.path.join(matrix_dir, "matrix.mtx.gz"))
print(mat)
mat.