# Brief Linear Algebra Note
## Matrix and Spaces

Matrix Multiplication:
 - Direct Compute: **Dot product of rows and columns**
 - Right multiplication: Linear combinations of columns
 - Left multiplication: Linear combinations of rows
 - Block matrix: Treat it as regular matrix

Elimination:
 - Find solution
 - Find null space
 - Find row space
 - Find inverse

LU-decomposition:
$$A = LU = \text{lower triangular} \cdot \text{upper triangular}$$
Not always working: need **permuting**.

4 spaces:
 - Column space
   - $\updownarrow$ transpose
 - Row space: find by elimination
   - $\updownarrow$ orthogonal complements
 - Null space: find by free columns
   - $\updownarrow$ transpose
 - Left null space

## Projection
Motivation: Column space are not always full rank and the nearest solution is **projection**.  
 - Single vector $a$:
    $$a^\top (b - ax) = 0 \Rightarrow x = \frac{a^\top b}{a^\top a} \Rightarrow \hat b = a \cdot \frac{a^\top b}{a^\top a} \Rightarrow P = \frac{aa^\top }{a^\top a}$$
 - Multi-vector $A$:
    $$A^\top (b - A\hat x) = 0 \Rightarrow \hat x = (A^\top A)^{-1}A^\top b \Rightarrow \hat b = A(A^\top A)^{-1}A^\top b \Rightarrow P = A(A^\top A)^{-1}A^\top $$
    $A^\top A$ is always full rank if $A$ is full column rank.  

## Orthonormal
Orthonormal **basis**: $Q^\top Q = I$.  
Orthogonal **matrix**: square, $Q^\top Q = QQ^\top = I \Rightarrow Q^\top  = Q^{-1}$.  
Unitary **matrix**: square, $Q^H = Q^{-1}$.  
Gram-Schmidt Process: Remove projection, normalize, repeat.  
Decompose according to orthonormal basis: dot products.  
$$x = c_1q_1 + c_2q_2 + \cdots \Rightarrow q_1^\top x = c_1q_1^\top q_1$$

## Determinant
Important rules:
 - $\det I = 1$  
 - Exchange rows multiplies by $-1$  
 - Every row same except one: decomposable  
 - Elimination does not change determinant  

Important properties:
 - $A$ is invertible $\Leftrightarrow \det A \neq 0$  
 - Determinant of upper(lower)-triangular matrices is the product of the main diagonal  
 - $\det AB = \det A \det B$
 - $\det A^\top = \det A$
 - $\det A$ is the volume defined by the column vectors  

Cofactor matrix:  
$$C = (-1)^{i+j} \det M_{i, j} \rightarrow \text{submatrix of } A \text{ by erasing row } i \text{ and column } j$$
 - Inverse: $A^{-1} = (\det A)^{-1} C^\top$
 - Cramer's Rule: $x_i = \dfrac{\det B_i}{\det A}$, $B_i$ is $A$ but column $i$ replaced by $b$.  

## Eigenvector-values
Definition:  
$$Ax = \lambda x \quad (x \neq \mathbf 0)$$

Diagonalization:  
$$A = S^{-1}\Lambda S  = \text{inverse of } S \cdot \text{eigenvalues} \cdot \text{eigenvectors}$$