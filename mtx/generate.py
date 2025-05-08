import numpy as np
from scipy.io import mmwrite
from scipy.sparse import csr_matrix

# 행렬 크기와 sparsity 설정
n_rows = 2000  # 행의 수
n_cols = 2000  # 열의 수
sparsity = 0.10  # 희소도 (0.05는 5% 비율)

# 희소 행렬을 위한 임의의 위치 생성
size = n_rows * n_cols
num_nonzero = int(size * sparsity)  # 비어 있지 않은 원소의 수
row_indices = np.random.randint(0, n_rows, num_nonzero)
col_indices = np.random.randint(0, n_cols, num_nonzero)
data = np.random.rand(num_nonzero)  # 비어 있지 않은 원소들의 값

# 희소 행렬 생성
A = csr_matrix((data, (row_indices, col_indices)), shape=(n_rows, n_cols))

# 파일명에 n_rows, n_cols, sparsity를 문자열로 포함
filename = f"sparse_matrix_{n_rows}x{n_cols}_s{int(sparsity*100)}.mtx"

# .mtx 파일로 저장
mmwrite(filename, A)

print(f"Matrix saved as {filename}")
