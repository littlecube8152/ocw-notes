 
Texts wrapped in
> this style are the notes not included in the tape. 

Some order of contents might not match with the tape because I would like to put relevant contents together, place motivation before introducing something (why would you learn something for nothing?)



---
Linear algebra is a study about **linear equations**.
---

\[Lecture 01 starts here\]

## Linear equations

There are three perspective of a system of linear equations, say $m$ equations and $n$ variables,
1. **Row picture**. It is how we see the equations. In two dimensions, it looks like lines intersecting each others, and in three dimensions, it looks like plane intersecting each others.
2. **Column picture**. It is to treat the equations as linear combinations of vectors.
3. **Matrix picture**. It is to combine the two aforementioned picture into a matrix form. 

For equation $A\mathbf{x} = b$, we think it as "can $b$ be represented by linear combination of columns of $A$?"

Some examples.

|Row picture |Column picture |Matrix picture|
|:-|:-|:-|
|$\begin{cases}2x & -y & = 0 \\ x & + 2y & = 3 \end{cases}$|$x\begin{bmatrix}2\\ 1\end{bmatrix}+y\begin{bmatrix}-1\\ 2\end{bmatrix}=\begin{bmatrix}0\\ 3\end{bmatrix}$|$\begin{bmatrix}2 & -1\\ 1 & 2\end{bmatrix}\begin{bmatrix}x \\ y\end{bmatrix}=\begin{bmatrix}0\\ 3\end{bmatrix}$|
|$\begin{cases}2x & -y & & = 0 \\ -x & + 2y & -1z & = -1 \\  & -3y & +4z & = -4 \end{cases}$|$x\begin{bmatrix}2\\ 1\\ 0\end{bmatrix}+y\begin{bmatrix}-1\\ 2\\ -3\end{bmatrix}+z\begin{bmatrix}0\\ -1\\ 4\end{bmatrix}=\begin{bmatrix}0\\ -1\\ 4\end{bmatrix}$|$\begin{bmatrix}2 & -1 & 0\\ 1 & 2 & -1\\ 0 & -3 & 4\end{bmatrix}\begin{bmatrix}x \\ y\\ z\end{bmatrix}=\begin{bmatrix}0\\ -1\\ 4\end{bmatrix}$|

Can I solve every $A\mathbf{x} = b$ for every $b$?
Which is, do all the linear combinations of all columns of $A$ fills the whole dimension?

\[Lecture 02 starts here]
## Eliminations
How do we solve a system of equations algorithmic? Eliminations.
Our idea is to make the matrix $A$ triangular, so we can back-substitute the variables with ease.

Example.
Suppose the equation we would like to solve is 
$$\begin{cases}x & +2y & +z & = 2 \\ 3x & + 8y & +z & = 12 \\  & 4y & +z & = 2 \end{cases}$$
Then the matrix $A$ will be
$$A = \begin{bmatrix}1 & 2 & 1 \\ 3 & 8 & 1 \\ 0 & 4 & 1\end{bmatrix}$$
First, we aim to eliminate the first column, so we select row 1 column 1 as the pivot.
$$\begin{bmatrix}\mathbf{1} & 2 & 1 \\ 3 & 8 & 1 \\ 0 & 4 & 1\end{bmatrix}$$
Then we subtract three times row 1 from row 2, making row 2 column 1 zero.
$$\begin{bmatrix}\mathbf{1} & 2 & 1 \\ 3 & 8 & 1 \\ 0 & 4 & -4\end{bmatrix}\rightarrow\begin{bmatrix}\mathbf{1} & 2 & 1 \\ 0 & 2 & -2 \\ 0 & 4 & 1\end{bmatrix}$$
Row 3 column 1 is already zero so we do nothing here.
$$\begin{bmatrix}\mathbf{1} & 2 & 1 \\ 0 & 2 & -2 \\ 0 & 4 & 1\end{bmatrix}$$
Now we are left with two variables (column 2, 3) and two equations, (row 2, 3). We do what we have done recursively.
Select row 1 column 1 as the pivot.
$$\begin{bmatrix}\mathbf{1} & 2 & 1 \\ 0 & \mathbf{2} & -2 \\ 0 & 4 & 1\end{bmatrix}$$
Then we subtract two times row 2 from row 3 to eliminate the four.
$$\begin{bmatrix}\mathbf{1} & 2 & 1 \\ 0 & \mathbf{2} & -2 \\ 0 & 4 & 1\end{bmatrix}\rightarrow\begin{bmatrix}\mathbf{1} & 2 & 1 \\ 0 & \mathbf{2} & -2 \\ 0 & 0 & 5\end{bmatrix}$$
Then only one row and one column are left, and we are done!

Well, before we go to the solution to the original equation, let's see will the elimination work in every case?
Obvious no, if at some point we are not able to choose a pivot, that is, the column we are dealing with are left with all zeros.

Let's head back to the solution. We put the constant term in column 4 and solve it, this called **augmented matrix**.
$$\begin{bmatrix}\mathbf{1} & 2 & 1 & 2 \\ 3 & 8 & 1 & 12 \\ 0 & 4 & -4 & 2 \end{bmatrix}\rightarrow\begin{bmatrix}\mathbf{1} & 2 & 1 & 2 \\ 0 & \mathbf{2} & -2 & 6\\ 0 & 4 & 1 & 2\end{bmatrix}\rightarrow\begin{bmatrix}\mathbf{1} & 2 & 1 & 2 \\ 0 & \mathbf{2} & -2 & 6 \\ 0 & 0 & 5 & -10\end{bmatrix}$$
Now we know that
$$\begin{cases}x & +2y & +z & = 2 \\  & 2y & -2z & = 6 \\  &  & 5z & = -10 \end{cases}$$
Which has a (also the only) solution
$$\begin{cases}x = 2 \\ y = 1 \\ z = -2 \end{cases}$$

### Elimination Matrix
In the column picture, we take multiplying a matrix by a column matrix as **taking the linear combination of each column**.
Say we multiply
$\begin{bmatrix}a & b \\ c & d\\\end{bmatrix}\begin{bmatrix}2 \\ 3\end{bmatrix} = 2 \begin{bmatrix}a \\ c\end{bmatrix} + 3 \begin{bmatrix}b \\ d\end{bmatrix}$
and we get a column matrix.

Now we are dealing with mostly row operations, and if we multiplying a row matrix by a matrix, we are **taking the linear combination of each row**.
$\begin{bmatrix}2 & 3\end{bmatrix}\begin{bmatrix}a & b \\ c & d\\\end{bmatrix} = 2 \begin{bmatrix}a & b\end{bmatrix} + 3 \begin{bmatrix}c & d\end{bmatrix}$

**This is how we want the matrix multiplication to be. If we want column picture, we multiply on the right. If we want row picture, we multiply on the left. Matrix is a way to unite two different perspectives.** 

Head back to our elimination, how can we speak it in the language of matrix?
$E_{21}\begin{bmatrix}\mathbf{1} & 2 & 1 \\ 3 & 8 & 1 \\ 0 & 4 & -4\end{bmatrix} = \begin{bmatrix}\mathbf{1} & 2 & 1 \\ 0 & 2 & -2 \\ 0 & 4 & 1\end{bmatrix}$
We want that $E_{21}$ subtracts three times row 1 from row 2 and do nothing about other rows. We are doing row operations so we put it on the left side.
Recall that row matrices are "linear combinations of rows", so 
$E_{21} = \begin{bmatrix}1 & 0 & 0 \\ -3 & 1 & 0 \\ 0 & 0 & 1\end{bmatrix}$
Also for the second step, we want to find some $E_{32}$ satisfying 
$E_{32}\begin{bmatrix}\mathbf{1} & 2 & 1 \\ 0 & \mathbf{2} & -2 \\ 0 & 4 & 1\end{bmatrix} = \begin{bmatrix}\mathbf{1} & 2 & 1 \\ 0 & \mathbf{2} & -2 \\ 0 & 0 & 5\end{bmatrix}$
and it is
$E_{21} = \begin{bmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & -2 & 1\end{bmatrix}$

Let we denote the final result as $U$, then we know that
$E_{32}(E_{21}A) = U$
In fact, we can change the parentheses, which means
$(E_{32}E_{21})A = U$
is also correct, and we have a matrix $E = E_{32}E_{21}$ that does all the work.

\[Lecture 03 starts here]
## Matrix Multiplication
Say we multiply two matrices $A$ and $B$, and the result would be $C$.
Now we use the respective lowercase of the matrix name to represent its corresponding elements, for example, $a_{1, 2}$ means the element in $A$ at row 1 column 2.
1. **Multiply rows by columns - the definition**
	Two matrices can be multiplied together if their the number of the rows in the first one is the same with the number of the columns in the second one (which is kind of obvious if you look at the row picture or the column picture). 
	Let's say that $A$ is a $m$ by $n$ matrix (which means there are $m$ rows and $n$ columns in $A$) and $B$ is a $n$ by $p$ matrix.
	Then the result of multiplication $C = AB$, is a $m \times p$ matrix where each elements is defined as below:$$c_{i, j} = \sum_{k = 1}^n a_{i, k}b_{k, j}$$ Which is, for $c_{i, j}$, we take the $i$-th row of $A$ and the $j$-th row of $B$ and take their dot products.  
	$\begin{bmatrix} \ &\ &\  \\ - & - & - \\ \ &\ &\  \end{bmatrix}\begin{bmatrix}\ &|&\ \\ \ &|&\  \\ \ &|&\  \end{bmatrix} = \begin{bmatrix} \ &\ &\  \\ \ &\cdot &\ \\ \ &\ &\  \end{bmatrix}$
2. **Multiply columns by columns**
	Well, we can also take the column picture, where each column of $B$ produces a column which is the linear combination of the columns in $A$, and we concatenate them in order.  
	$\begin{bmatrix} - & - & - \\ - & - & - \\ - & - & - \end{bmatrix}\begin{bmatrix}\ &|&\ \\ \ &|&\  \\ \ &|&\  \end{bmatrix} = \begin{bmatrix} \ &|&\  \\ \ &|&\ \\ \ &|&\  \end{bmatrix}$
3. **Multiply rows by rows**
	Row picture also works this way, and it is clear so there is going to be only illustrations.  
	$\begin{bmatrix} && \\ - & - & - \\ && \end{bmatrix}\begin{bmatrix} |&|&| \\ |&|&| \\ |&|&| \end{bmatrix} = \begin{bmatrix} && \\ -&-&- \\ &&  \end{bmatrix}$
4. **Multiply columns by rows**
	What if we do the only left possibility, multiply columns by rows?  
	In this way, we take the $k$-th row of $A$ and the $k$-th row of $B$ and they multiply into a $m\times p$ matrix.  
	And we have $n$ of them, adding them up we get $C$ in the end.  
	In computers, this is the best way we have since it has the best cache.  
5. Block Multiplication
	Instead of doing the full matrix multiplication at once, we can chop them into chunks, say we have
	$A = \begin{bmatrix}A_1 & A_2 \\ A_3 & A_4 \end{bmatrix}, B = \begin{bmatrix}B_1 & B_2 \\ B_3 & B_4 \end{bmatrix}$  
	As long as the size is consistent with each others, we can do multiplication in this way:
	$C = \begin{bmatrix}A_1B_1 + A_2B_3 & A_1B_2 + A_2B_4 \\ A_3B_1 + A_4B_3 & A_3B_2 + A_4B_4\end{bmatrix}$  
	which is kind of, resembling the $2\times 2$ multiplication.

## Inverse (of square matrices)
For every square matrix $A$, is there another matrix $A^{-1}$ satisfying $A^{-1}A = I$?  
If $A^{-1}$ does exist, then $A^{-1}A = I = AA^{-1}$.

For those which have an inverse, they are called **invertible matrices** or **non-singular matrices**.
For those which do not have an inverse, they are called **singular matrices**.

**Property.** A matrix $A$ is singular matrix if there is a non-zero $\mathbf{x}$ satisfies $A\mathbf x = \mathbf 0$.  
> Assume that $A^{-1}$ exists, then we have $A^{-1}A\mathbf x = A^{-1} \mathbf 0$, which means $\mathbf x = \mathbf 0$ and we get a contradiction.

> Thus we know for each column matrix of size $n$, $A$ is a way to map each column matrix to another matrix, such that no two matrices have the same output.
> Assume that $A^{-1}$ exists, then $A$ and $A^{-1}$ can be treated as two functions which are the inverse of each other, thus $AA^{-1} = I = A^{-1}A$.  
> Also we can imply that the property is actually the sufficient and necessary condition of singular matrices.  

Let's take a look of $2\times 2$ matrices, when does $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ have an inverse?  
$AA^{-1} = I$, which means there is a solution for the two system:  
$\begin{bmatrix} a & b \\ c & d \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$  
$\begin{bmatrix} a & b \\ c & d \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$  
When we expand it, they have the same coefficient for the $x$ and the $y$ terms, but not the constant ones.
Then we are going to introduce Gauss-Jordan Elimination, which is capable of solving multiple system with the same coefficient of variables at the same time.

### Gauss-Jordan Elimination
In order to find the inverse, we put $A$ on the left side and $I$ on the right side, combined into a single long matrix (an **augmented matrix**).  
$$[A|I]$$  
And we keep doing row operations, until the left side becomes $I$ and the right side is $A^{-1}$. Why is that?  
Recall row operations are matrices, let's say we have done $E_1, E_2, \cdots, E_k$ in order. Since we are in row pictures, we can break the augmented matrix into two matrices, and because of the associative law, we denote $E$ as $E_kE_{k-1}\cdots E_1$.  
Then we have $EA = I$, which means $E = A^{-1}$ and on the right side we have $A^{-1}I = A^{-1}$, which is why it works magically for every invertible matrix.

\[Lecture 04 starts here]
### More inverses
Inverse of $AB$? $B^{-1}A^{-1}$. (Check it for both sides!)  
Inverse of $A^{T}$?  
$(A^{-1}A)^\top  = I^\top $  
$A^\top (A^{-1})^\top  = I$  
Therefore it is $(A^{-1})^\top $.  

## LU-factorization (decomposition)
> Purposes of $LU$-factorization:
> 1. It is another way to interpret Gauss Elimination.
> 2. In computation, for a fixed $A$, a $n\times n$ matrix, solving $Ax = b$ is $\mathcal O(n^3)$ each time. However for upper-triangle matrices and lower-triangle matrices, solving $Lx = b$ or $Ux = b$ is $\mathcal O(n^2)$ (because the elimination is easier each steps, almost identical to back substitution). Since in many applications of linear algebra, $A$ is fixed during the whole procedure, $LU$ decomposition comes in handy since it reduces time significantly.  
> 	Notice that even we have the inverse matrix, matrix multiplication still takes $\mathcal O(n^\omega)$ time and $LU$-factorization is still far better (at least at the moment I am writing this note).

Recall what we have learnt about elimination, our goal is
$$A = LU$$
How do we find $L$? We already have the elimination matrices:
$$E_kE_{k-1}\cdots E_1A = U$$
For these elimination matrices, they are easy to "undo" them. Every row operation we have done is subtract $k$ times row $i$ from row $j$. To undo it, we just add back $k$ times row $i$ to row $j$, and it is easy to verify this is the inverse matrix.
Therefore we can do this:
$$E_1^{-1}\cdots E_{k-1}^{-1}E_k^{-1}E_kE_{k-1}\cdots E_1 A = E_1^{-1}\cdots E_{k-1}^{-1}E_k^{-1}U$$
And we have 
$$A = E_1 A = E_1^{-1}\cdots E_{k-1}^{-1}E_k^{-1}U = LU$$
which means 
$$L = E_1^{-1}\cdots E_{k-1}^{-1}E_k^{-1}$$
For now, we ignore the troublesome matrices, which gives zero when performing elimination. 
The cool thing is, multiplying any two lower-triangular matrices obtains another lower-triangular matrix, so $L$ must be a lower-triangular matrix.  
And if we want there are all $1$s in the main diagonal, we can always do
$$A = LDU$$
where $D$ is a diagonal matrix (which means any elements not lying on the main diagonal is zero).

\[Lecture 05 start here]
### Permuting allowed
Sometimes $A$ is good enough to perform elimination without failing to pick a pivot, but for all invertible matrices, it is not always the case.
Therefore we are introducing the idea of permutation matrices. With permuting allowed, every invertible matrix is able to do the LU-factorization.
$$PA = LU$$
A permutation matrix $P$ is a square matrix which has exactly one $1$ in each row and column, and other elements are all $0$.
In the previous section, $P = I$, which means no row exchanges are performed.
From the row picture, we can see what $P$ does is exactly permuting the rows.
A cool fact is that, the inverse of $P$, $P^{-1}$, is actually identical to the transpose of $P$, $P^\top$.

## Transpose
Basic rule:
$$(AB)^\top  = B^\top A^\top $$
Symmetric matrices are the matrices satisfying
$$A = A^\top $$
And we have the following property:
**Property.** For any matrix $A$, $AA^\top$ is symmetric.
*Proof.* 
$$(AA^\top )^\top  = A^{\top\top}A^\top  = AA^\top $$
\[Lecture 06 starts here]
## Vector Spaces - A Generalization of Vectors
A vector space is a set of vectors which supports scalar multiplication and addition (which is what we have used to solve linear equations so far).
To generalize the idea, a vector space is a set of vectors $V$ over a field $F$.
It has to support the following axioms.

The first two are operations, and the remain eight are vector space axioms. 
If not mentioned, we assume it should be hold for any $a, b \in F$ and $u, v, w \in F$.

|Meaning |Definition |
|-|-|
|Addition |$u + v \in V$|
|Scalar Multiplication |$au \in V$|
|Associativity|$u + (v + w) = (u + v) + w$|
|Commutativity|$u + v = v + u$|
|Identity element (of addition)|$\exists \mathbf 0 \in V$ s.t. $v + \mathbf 0 = v$|
|Identity element (of multiplication)|$\exists 1 \in F$ s.t. $1v = v$|
|Inverse elements|$\exists -v \in V$ s.t. $v + (-v) = \mathbf 0$
|Compatibility (of scalars)\*|$(ab)v = a(bv)$
|Distributivity (of vectors)|$a(u+v) = au + av$
|Distributivity (of scalars)|$(a + b)v = av + bv$

\* Note: associativity of scalars are defined by fields, and vector spaces are good with the non-associative fields.

There are many examples. In fact, for any positive integer $n$, $\mathbb R^n$ is a vector space over $\mathbb R$ (and it is easy to verify that).

### Subspaces
**Definition.** A set $S \subset V$, where $V$ is a vector space over $F$, is called a subspaces if $S$ is a vector space over $F$ with the same addition and scalar multiplication operations.

**Property.** For two subspaces of $V$, say $S$ and $T$, their intersection forms another subspace, but their union is not always another subspace.

Notice that when regarding subspaces, many of the axioms are actually applied to the operations directly, so we can only check if the addition and scalar multiplication is closed in the set and zero is present.

### Column Spaces
Assume we are in $\mathbb R^n$, a $n\times m$ matrix $A$ forms a column space, which is a subspace of $\mathbb R^n$, defined as follows:
$$C(A) = \{\mathbf v | \exists C_{1\times m} \text{ s.t. } AC = \mathbf v\}$$
In other words, we put all linear combinations of columns of $A$ in the set.
Now we start to think of, does $C(A)$ fill the whole $\mathbb R^n$? If not always, how much is $C(A)$ filling?
The answer is,
$$C(A) = \{b | Ax = b \text{ has a solution}\}$$
which is equivalent to the definition above.

### Null Spaces
Assume we are in $\mathbb R^m$, a $n\times m$ matrix $A$ not only forms a column space but also forms a **null space**, which is a subspace of $\mathbb R^m$, defined as follows:
$$N(A) = \{\mathbf x | A\mathbf x = \mathbf 0\}$$
$\mathbf 0$ is definitely in the set. For any scalars, $c\mathbf x$ is still in the set, and for any vectors, their combination, say $A(\mathbf x + \mathbf y)$, still equals to $\mathbf 0$.

\[Lecture 07 starts here]
> Why is null spaces important?  
> As mentioned before, with $\mathcal O(n^3)$ pre-processing, we can obtain any solution of $Ax = b$ under $\mathcal O(n^2)$. Well, that applies only if $A$ is invertible.  
> With null spaces, we can know if $Ax = b$ has a unique solution, and if not, we can even know all the solutions under $\mathcal O(n^2)$. Back-substitution takes $\mathcal O(n^3)$ if there are more than one solution (since in $i$-th step there are at most $i$ free variables, and back-substitution would take $\mathcal O(i^2)$ times. Summing them up gets $\mathcal O(n^3)$.)

#### Row Echelon Form

Now we try to find null spaces of a matrix, and we need a working algorithm.
Let's start with an example, say
$$A = \begin{bmatrix}1 & 2 & 2 & 2 \\ 2 & 4 & 6 & 8 \\ 3 & 6 & 8 & 10\end{bmatrix}$$
Now we try to apply elimination, since for any elimination matrix or permutation matrix $E$,
$$Ax = \mathbf 0 \Rightarrow EAx = E \mathbf 0 = \mathbf 0$$
the algorithm still works, so let's see.
$$\begin{bmatrix}1 & 2 & 2 & 2 \\ 2 & 4 & 6 & 8 \\ 3 & 6 & 8 & 10\end{bmatrix} \rightarrow \begin{bmatrix}1 & 2 & 2 & 2 \\ 0 & 0 & 2 & 4 \\ 0 & 0 & 2 & 4\end{bmatrix} \rightarrow \begin{bmatrix}1 & 2 & 2 & 2 \\ 0 & 0 & 2 & 4 \\ 0 & 0 & 0 & 0\end{bmatrix} = U$$
We call the result $U$, a matrix with a staircase-looking zeroes, is the **(row) echelon form**.
This matrix represents
$$\begin{cases}x_1 & +2x_2 & +2x_3 & +2x_4 & = 0 \\ && 2x_3 & +2x_4 & = 0 \end{cases}$$
which only have 2 equations but 4 unknowns, and it seems there is still a lot of space left for the solutions.  
Therefore we introduce how do we describe "how free the solutions are".  
The **rank** of $A$ is defined as the number of pivots during the elimination.
And we say the columns which contains pivots are **pivot columns** and the rest of them are **free columns**.  
Why is it called **free columns**? Because they does not contain important pivots, and we could cancel out them by adjusting pivot columns.  
What it takes to eliminate 1 column 2? We take negative 2 times of column 1, therefore one of the solutions is
$$x = \begin{bmatrix}-2 \\ 1 \\ 0 \\ 0\end{bmatrix}$$
What it takes to eliminate 1 column 4? We take negative 2 times of column 3 and 2 times of column 1, therefore another solution is
$$x = \begin{bmatrix}2 \\ 0 \\ -2 \\ 1\end{bmatrix}$$
And we could take all of the linear combinations, thus the null space of $A$ is
$$x = c\begin{bmatrix}-2 \\ 1 \\ 0 \\ 0\end{bmatrix} + d\begin{bmatrix}2 \\ 0 \\ -2 \\ 1\end{bmatrix}$$
What does "rank" mean? It means there are $n - \mathrm{rank}(A)$ number of free columns, which means the solutions are the linear combinations of these $n - \mathrm{rank}(A)$ vectors. In this case, we have $2$ of them.

#### Reduced Row Echelon Form
Actually, we can do more. Continuing from the previous matrix $A$, we already have
$$\begin{bmatrix}1 & 2 & 2 & 2 \\ 2 & 4 & 6 & 8 \\ 3 & 6 & 8 & 10\end{bmatrix} \rightarrow \begin{bmatrix}1 & 2 & 2 & 2 \\ 0 & 0 & 2 & 4 \\ 0 & 0 & 2 & 4\end{bmatrix} \rightarrow \begin{bmatrix}1 & 2 & 2 & 2 \\ 0 & 0 & 2 & 4 \\ 0 & 0 & 0 & 0\end{bmatrix} = U$$
We eliminate more, making all pivot columns left with only single one.  
$$U = \begin{bmatrix}1 & 2 & 2 & 2 \\ 0 & 0 & 2 & 4 \\ 0 & 0 & 0 & 0\end{bmatrix} \rightarrow \begin{bmatrix}1 & 2 & 0 & -2 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0\end{bmatrix} = R$$
We call $R$ **row reduced echelon form** of $A$, denoted by $R = \mathrm{rref}(A)$.
The idea is when we are finding the way to balance out the effect by picking some free columns, we have to pick exactly negative amount of these pivot columns, and the solutions can be seen with ease by this way.  
Let's suppose $R$ is in this form:
$$R = \begin{bmatrix} I & F \\ \mathbf 0 & \mathbf 0 \end{bmatrix}$$
Where $I$ are the pivot columns and $F$ are the free columns, then the null space of $R$ is the column space of
$$N = \begin{bmatrix} -F \\ I \end{bmatrix}$$

Another example, suppose $A$ is
$$A = \begin{bmatrix}1 & 2 & 3 \\ 2 & 4 & 6 \\ 2 & 6 & 8 \\ 2 & 8 & 10 \end{bmatrix}$$
Then we have 
$$U = \begin{bmatrix}1 & 2 & 3 \\ 0 & 2 & 2 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$$
and also
$$R = \begin{bmatrix}1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$$
The rank is $2$, and there are going to be $1$ free columns. The solutions are
$$x = c\begin{bmatrix}-1 \\ -1 \\ 0\end{bmatrix}$$
You see the formula we just obtained also works here.

\[Lecture 08 starts here]

#### Finding Solutions
We already solved all solutions to $Ax = \mathbf 0$, then what about the general problem: solving $Ax = b$?
What are the solutions? How many are them? Or do they even exist?
- Existence
	$b$ has a solution if and only if the augmented matrix $[A|b]$ does not have any row with all zeroes in $A$ but non-zero in $b$.
- Uniqueness
	If $b$ has a solution, then after elimination (into rref), we can obtain a solution $x_{p}$ only using the pivot rows. The full solution to the equation $Ax = b$ is every element in $x_p + x_n$ where $x_n$ is the null space.

Some special cases:
- Full row rank matrices $r = m < n$
	Every $b$ has a solution, and there are infinitely many solutions for every $b$.
- Full column rank matrices $r = n < m$
	For every $b$ has a solution, there is exactly one solution.
- Full rank matrices $r = n = m$
	For every $b$, there is a unique solution. In other words, the matrix is invertible.

\[Lecture 09 starts here]

## Independence, span and basis

Suppose $A$ is a $m$ by $n$ matrix with $m < n$.  
Then there are non-zero solutions to $Ax = \mathbf 0$! (since there are always free variables).

### Independent
**Definition.** Vector $v_1, v_2, \cdots, v_n$ are called **`(linearly) independent** if no non-zero combination of them gives $\mathbf 0$. Otherwise, they are called **(linearly) dependent**.  

**Property.** Let $v_1, v_2, \cdots, v_n$ be the columns of $A$. These vectors are independent if $N(A) = \{\mathbf 0\}$, which means $\mathrm{rank}(A) = n$ and dependent if otherwise.  
It is easy to see that property is true.  

### Span
**Definition.** Vector $v_1, v_2, \cdots, v_n$ **span** a vector space which is the set of all linear combinations of the vectors.  

As column vectors, we can say if $v_1, v_2, \cdots, v_n$ are the columns of $A$, then $v_1, v_2, \cdots, v_n$ span $C(A)$.

### Basis
**Definition.** For a vector space $V$, $v_1, v_2, \cdots, v_n$ is called the **basis** of the space if
 1. $v_1, v_2, \cdots, v_n$ are independent.  
 2. $v_1, v_2, \cdots, v_n$ span $V$.  

Example. 
$\begin{bmatrix}1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix}0 \\ 1 \\ 0 \end{bmatrix}, \begin{bmatrix}0 \\ 0 \\ 1 \end{bmatrix}$ span $\mathbb R^3$.

**Property.** $n$ vectors gives a basis of the $n\times n$ matrix containing them as columns is **invertible**.  

### Dimension
**Property.** Every basis of the vector space has same number of vectors.  
*Proof.* Suppose a basis $b'$ is bigger than the other basis $b$, then we can know after elimination, $b'$ should have null space other than $\{\mathbf 0\}$.  

Therefore we can now tell how *big* a vector space is.  
**Definition.** The dimension of a vector space, called $\dim V$, is defined as the size of its basis.  
**Property.** $\dim C(A) = \mathrm{rank}(A)$.

Keypoint: if you already know the dimension of $V$, then every independent $\dim V$ vectors in $V$ is a basis.  

**Property.** Suppose $A$ is a $n \times m$ matrix. $\dim N(A) = \#\text{free variables}$, $\dim N(A) + \dim C(A) = m$.

\[Lecture 10 starts here]

## Four Important Spaces
Suppose $A$ is a $m \times n$ matrix.
 1. Column space $C(A) \subset \mathbb R^m$
 2. Null space $N(A) \subset \mathbb R^n$
 3. Row space $C(A^\top )  \subset \mathbb R^n$
 4. Left null space $N(A^\top )  \subset \mathbb R^m$

We aleady know how to find the first two. What about the rest?

### Row space
We are interested in what vectors can these rows span?  
The idea is, **when applying row operations, the row space does not change**.  
Then we are just going to find the row reduced echelon form, and the non-zero rows form a basis.  

> The reason why this is correct.  
> All the zero rows was a linear combination of the rest before elimination. Thus if them remain, these row vectors are dependent, and we can delete them safely.  
> Also, we don't reduce the dimension of the row space. Think about it intuitively, if the rest are independent, then replace one as itself add others should not make the new vectors dependent.  

Say $A = \begin{bmatrix} 1 & 2 & 3 & 1 \\ 1 & 1 & 2 & 1 \\ 1 & 2 & 3 & 1\end{bmatrix}$, then $\mathrm{rref}(A) = \begin{bmatrix} 1 & 0 & 1 & 1 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0\end{bmatrix}$. Thus the row space has a basis of $\begin{bmatrix} 1 & 0 & 1 & 1 \\ 0 & 1 & 1 & 0 \end{bmatrix}$.  

### Left null space
The reason it is called *left* null space is because, it contains all elements $y$ satisfying
$$A^\top y = \mathbf 0$$
Transpose both side yields
$$y^\top A = \mathbf 0^\top $$
which resembles the definition of null space but the vector is on the left side.  

How do we find it? Well, now we are interested in **what linear combinations of rows gives a zero row**.  

We know they are going to be some (or none) after we reduce them into row reduced echelon form, but what are these? We need the elimination matrix.  
Let's use that augmented thing again.  
$$[A|I] \rightarrow [R|E]$$  
Then we know for each zero row of $R$, the corresponding row of $E$ tells us what combination can we have this zero, and collecting all of them gives the left null space.  

For example, take $A = \begin{bmatrix} 1 & 2 & 3 & 1 \\ 1 & 1 & 2 & 1 \\ 1 & 2 & 3 & 1\end{bmatrix}$ again. $E$ is going to be $\begin{bmatrix} -1 & 2 & 0 \\ 1 & -1 & 0 \\ -1 & 0 & 1\end{bmatrix}$. Therefore the left null space has the basis of $\begin{bmatrix}-1 & 0 & 1\end{bmatrix}$.  

### Dimension relation
The following relation holds:
$$\dim C(A) + \dim N(A) = n$$
$$\dim C(A^\top ) + \dim N(A^\top ) = m$$
$$\dim C(A) = \dim C(A^\top )$$
The first two are pretty obvious according to the definition, and the last can be observed that the pivot columns have the same number of non-zero rows, thus they have the same dimension.  

\[Lecture 11 starts here]

### Other Spaces
Let $M$ be the set of all $3\times 3$ matrices. Is $M$ a vector space? Yes.  
In fact there are several subspaces, such as $U$, the set of all upper triangular matrices, and $S$, the set of all symmetric matrices.  

We know that $\dim M = 9, \dim S = 6, \dim U = 6$, and there is more than that.  
Let $D = S \cap U$, then $D$ contains all diagonal matrices and $\dim D = 3$.  
Let $A = S + U$, then $A$ is $M$ and $\dim A = 9$.  
A cool relation is that, $\dim S + \dim D = \dim (S \cap D) + \dim (S + D)$. Is that always true?  

Another example: let $S$ be all of the solutions $y$ to the equation
$$\frac{\mathrm d^2y}{{\mathrm dx}^2} + y = 0$$

> In differential equations, we will know that the solution space has dimension $2$. Now we assume that is true and think of it later in calculus class.  

There are two special solutions: $y = \cos x, \sin x$.  
And they span the whole solution space $S$.

### Rank 1 matrices

Every rank 1 matrix can be expressed by a column matrix times a row matrix.  

> It is easy to see that: pick the first non-zero column and the first non-zero row, since its rank has to be 1 and all of the rows and columns must be some constant times a scalar.  

\[Lecture 12 starts here]

## Applications
### Graph Potential - Currents and Kirchhoff's Law
Graph is formed by a set of vertices and a set of edges, used to represent abstract idea of real world connection models. In this case, we are going to discuss **potential**, for example, electrical potential in circuit.  

Let's talk about this graph $G$, it has $n = 4$ nodes and $m = 5$ edges.  

```
1--→4
|\  ↑
| \ |
↓  ↘|
2--→3
```

We define the **incidence matrix** $A$ of the graph as a $m\times n$ matrix, where each row represent a edge.  
$$A = \begin{bmatrix}-1 & 1 & 0 & 0 \\ 0 & -1 & 1 & 0 \\ -1 & 0 & 1 & 0 \\ -1 & 0 & 0 & 1 \\ 0 & 0 & -1 & 1\end{bmatrix}$$

Why this is important? We will see a few applications.  

- Potentials  
  Let's say each vertex has its own *potential*. Therefore the difference of potential of each edge (which indicates how likely or how strong power is going down the edge), is the incidence matrix $A$ multiplies the potential column matrix $x$. In this example, it is
  $$\begin{bmatrix}-1 & 1 & 0 & 0 \\ 0 & -1 & 1 & 0 \\ -1 & 0 & 1 & 0 \\ -1 & 0 & 0 & 1 \\ 0 & 0 & -1 & 1\end{bmatrix}\begin{bmatrix}x_1 \\ x_2 \\ x_3 \\ x_4\end{bmatrix}$$
  Solving $Ax = \mathbf 0$ gives us some possiblilties of stable state. More specifically, the set of all stable states is the null space $N(A)$. 
- Currents  
  In circuits, these edges are wires and some currents run through them. In this case, the potential of each node should have net difference of zero. Therefore it is stated by the equation  
  $$ A^\top y=\mathbf 0$$
  $$\begin{bmatrix}-1 & 0 & -1 & -1 & 0 \\ 1 & -1 & 0 & 0 & 0 \\ 0 & 1 & 1 & 0 & -1 \\ 0 & 0 & 0 & 1 & 1 \end{bmatrix}\begin{bmatrix}y_1 \\ y_2 \\ y_3 \\ y_4 \\ y_5\end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \\ 0\end{bmatrix}$$
  Solving the left null space, $N(A^\top )$, tells us what are the stable states. In fact, the basis of the null space are *circuits* (or called *cycles*).  
  Assume the graph is *connected*, we have the following identity:
  $$\text{\#nodes } - \text{\#edges +} \dim N(A^\top ) = 1$$ 
  In physics, this is called **Kirchhoff's Current Law**.  

Using Ohm's Law, the two aspects of incidence matrix can be united into a single equation.  

\[Lecture 13 is about Quiz 1]  
\[Lecture 14 starts here]

## Orthogonality

Two column matrices $x, y$ are called **orthogonal** ($x \perp y$) if
$$x^\top y = \mathbf 0$$

**Property.** Let $\|x\|^2 = x^\top x$. $x$ and $y$ are orthogonal if and only if
$$\|x\|^2 + \|y\|^2 = \|x+y\|^2$$
*Proof.* Expand RHS gives 
$$x^\top x + x^\top y + y^\top x + y^\top y = x^\top x + y^\top y = \|x\|^2 + \|y\|^2$$

**Definition.** Subspace $S$ is called **orthogonal to** subspace $T$ if 
$$\forall s \in S, \forall t \in T, s^\top t = \mathbf 0$$

For example,  
**Property.** For the same matrix $A$, row space is orthogonal to the null space.  
*Proof.* Recall the definition of null space:
$$Ax = \mathbf 0$$
Thus for every row $u$ and every element $x$ in the null space, we have
$ux = \mathbf 0$
Since row space only contains linear combinations of the rows, they all satisfy the condition.  
Formally, let's say $A$ is $m \times n$, and we denote row $i$ by vector $u_i$. For each element $v$ in the row space, we can find $m$ real numbers $c_1, c_2, \cdots, c_m$ satisfying
$$c_1 u_1 + c_2 u_2 + \cdots + c_m u_m = u$$
Therefore, for any element $x$ in the null space,
$$u^\top x = (c_1 u_1 + c_2 u_2 + \cdots + c_m u_m)^\top x = 0 + 0 + \cdots + 0 = 0$$
For the same reason, column space is orthogonal to the left null space.  

Not only they are orthogonal, they are *orthogonal complements* in $\mathbb R^n$, which means null space contains *all* vectors that are orthogonal to the (all the elements in) the row space and vice versa.  

\[Lecture 15 starts here]
## Projection
### Motivation
Using the knowkledge we've know so far, it is possible that
$$Ax = b$$
does not have a solution, and it is bugging.  
Sometimes we want something that is *the nearest* solvable $b$. For example, we want to find a line through $(1, 1), (2, 2), (3, 2)$, but it is certainly impossible. Then we start to think, if we are going to find a line that is closest to the ideal one, what would it be?  
It turns out we want to solve it as
$$\begin{bmatrix} 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{bmatrix}\begin{bmatrix} a \\ b \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \\ 2 \end{bmatrix}$$
but as we can see it has no solution.  
Projection, is the tool that enables us project any $b$ onto the $C(A)$ in a formulated manner, and it is invented to solve many problems, including this one.  

### Projections onto Subspaces
#### 2D cases
Let's say $a, b$ are two vectors. What does it mean to *project* $b$ onto $a$?  
We want to find some $p = xa$, and the error $b - p$, should perpendicular (or *orthogonal*) to $a$. In the language of math, 
$$a^\top (b - xa) = \mathbf 0$$
Solving it yields
$$a^\top b = xa^\top a \Rightarrow x = \frac{a^\top b}{a^\top a} \Rightarrow p = a \cdot \frac{a^\top b}{a^\top a}$$
There is something noteworthy, that is, if we re-write the equation as
$$p = \frac{aa^\top }{a^\top a}\cdot b$$
This gives a matrix $P = \dfrac{aa^\top }{a^\top a}$ which does the projection work!
Also we have the following identity:  
**Property.** Assume $P$ is a projection matrix, then  
1. $P$ is symmetric.  
2. $P^2 = P$.  
3. $\dim C(P) = 1$ if $a \neq \mathbf 0$

*Proof.* 
1. $P^\top  = \dfrac{(aa^\top )^\top }{a^\top a}= \dfrac{a^{\top\top}a^\top }{a^\top a} = \dfrac{aa^\top }{a^\top a} = P$
2. In geometric perspective, projecting a vector twice does the same thing of projecing it once. In explicit definition,
   $P^2 = \dfrac{aa^\top }{a^\top a}\dfrac{aa^\top }{a^\top a} = \dfrac{a}{a^\top a}\dfrac{a^\top a}{a^\top a}\dfrac{a^\top }{1} = \dfrac{aa^\top }{a^\top a} = P$  
3. It is pretty obvious by the definition: every row is a multiple of $a^\top$. Moreover, $C(P) = \{ca\}$.  

#### 3D cases
Let's say there are two vectors $a_1, a_2$ and they form a plane. How do we project any $b$ onto the plane?  
We want to find some $p$ which is the linear combination of $a_1$ and $a_2$, and the error $b - p$, should perpendicular (or *orthogonal*) to $a_1$ and $a_2$. In the language of math, let
$$p = x_1 a_1 + x_2 a_2$$
we could re-write that as
$$p = \underbrace{\begin{bmatrix} & \\ a_1 & a_2 \\ & \\\end{bmatrix}}_A\underbrace{\begin{bmatrix}x_1 \\ x_2\end{bmatrix}}_{\hat x}$$
$$\begin{cases}a_1^\top (b - A\hat x) & = \mathbf 0 \\ a_2^\top (b - A\hat x) & = \mathbf 0  \end{cases}$$
In matrix form, 
$$ \underbrace{\begin{bmatrix} & a_1^\top  & \\ & a_2^\top  & \\\end{bmatrix}}_{A^\top }\left(b - \underbrace{\begin{bmatrix} & \\ a_1 & a_2 \\ & \\\end{bmatrix}}_A\begin{bmatrix}x_1 \\ x_2\end{bmatrix}\right) = \mathbf 0$$
$$A^\top b = A^\top A\hat x$$
Notice that the error $b-A\hat x$ is in $N(A^\top )$ (which is kind of intuitive: we restrict it to perpendicular to the column space).  
If the inverse of $AA^\top$ exists, then we can find
$$p = A\hat x = A(A^\top A)^{-1}A^\top b$$

\[Lecture 16 starts here]

What is happening in the projection matrix $P = A(A^\top A)^{-1}A^\top$?
 - If $b$ is orthogonal to the column space, then $A^\top b = \mathbf 0$, giving $p = \mathbf 0$.  
 - If $b$ is in the column space, then there exists $Ax = b$, then $p = Pb = Ax = b$.  

We can see that we are actually finding two projections: $b = p + e$ and $p \in C(A), e \in N(A^\top)$.  

**Property.** If $A$ has independent columns, then $A^\top A$ is invertible.  
*Proof.* Suppose $A^\top Ax = \mathbf 0$, then we want to show that $x = \mathbf 0$.  
BRILLIANT IDEA: multiply both side by $x^\top $ on the left.  
$$x^\top A^\top Ax = \mathbf 0$$
Therefore 
$$(Ax)^\top (Ax) = \mathbf 0 \Rightarrow \|Ax\| = 0 \Rightarrow Ax = \mathbf 0$$
Since $A$ has independent columns, its null space is $\{\mathbf 0\}$. Thus $x = \mathbf 0$.  

### Application - Smallest Square
Let's head back the example we left as describing why projection is important and actually solve it.  

**Property.** If $b = p + e$ and $p \in C(A)$, then $e$ attains its minimum length ($\|e\|$) if $e \in N(A^\top )$.  
It is kind of intuitive, if $e$ is not then we can always extract the part in column space and get a smaller one.  

In 2D, we are going to find a line $a + bt$ to make the error as small as possible. The points were $(1, 1), (2, 2), (3, 2)$, thus
$$\begin{bmatrix} 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{bmatrix}\begin{bmatrix} a \\ b \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \\ 2 \end{bmatrix}$$
and to solve it to the best,
$$\begin{bmatrix} 
	1 & 1 & 1 \\ 1 & 2 & 3 
\end{bmatrix}\begin{bmatrix} 
	1 & 1 \\ 
	1 & 2 \\ 
	1 & 3 
\end{bmatrix}\begin{bmatrix} 
	a \\ b 
\end{bmatrix} = \begin{bmatrix} 
	1 & 1 & 1 \\ 
	1 & 2 & 3 
\end{bmatrix}\begin{bmatrix} 
	1 \\ 2 \\ 2 
\end{bmatrix}$$
$$\begin{bmatrix} 
	3 & 6 \\ 6 & 14
\end{bmatrix}\begin{bmatrix} 
	a \\ b 
\end{bmatrix} = \begin{bmatrix} 
	5 \\ 11
\end{bmatrix}$$
which gives $a = \frac 2 3, b = \frac 1 2$.  

> There is another calculus approach: since the least square is a quadratic function, taking its (partial) derivative is not a hard work.  

\[Lecture 17 starts here]

### Orthonormal basis and matrix
A basis $q_1, q_2, \cdots, q_n$ is called a **orthonormal basis** if $q_i^\top q_j = \begin{cases} 0 & \text{if } i \neq j \\ 1 & \text{if } i = j\end{cases}$.  
A **square** matrix is **orthonormal (orthogonal)** if its columns are orthonormal basis.  

**Property.** Let $q$ be a orthonormal basis, and $Q = \begin{bmatrix}q_1 & q_2 & \cdots & q_n\end{bmatrix}$, then $Q^\top Q = I$.  
**Property.** Let $Q$ be a orthonormal matrix, then $Q^\top  = Q^{-1}, Q^\top Q = QQ^\top  = I$.

Why are we discussing orthonormal basis? It turns out when dealing with projections,  
$$P = Q(Q^\top Q)^{-1}Q^\top  = QQ^\top $$
$$Q^\top Q\hat x=\hat x=Q^\top b$$
If we could, somehow turn every matrix $A$ into orthonomal basis $Q$, then projection is very easy.  

### Gram-Schmidt Process
Goal: turn every matrix $A$ whose columns are independent into matrix $Q$ formed by orthonormal column vectors.  
Idea: The first vector can stay, and for each new vector we meet, we subtract its projection to every previous vector. Finally, divide every vector by their length.  

Suppose we have $v_1, v_2, v_3$.  
 - $u_1 = v_1$
 - $u_2 = v_2 - \dfrac{u_1^\top v_2}{u_1^\top u_1}u_1$  
 - $u_3 = v_3 - \dfrac{u_1^\top v_3}{u_1^\top u_1}u_1 - \dfrac{u_2^\top v_3}{u_2^\top u_2}u_2$  

Then $q_1 = \dfrac{u_1}{\|u_1\|}, q_2 = \dfrac{u_2}{\|u_2\|}, q_3 = \dfrac{u_3}{\|u_3\|}$.  

\[A section from lecture 24 inserted]
### Fourier Series

If we have all orthonormal vectors in a vector space, when computing
$$v = c_1q_1 + c_2q_2 + \cdots c_nq_n$$
We can do
$$q_i^\top v = c_1q_i^\top q_1 + c_2q_i^\top q_2 + \cdots c_nq_i^\top q_n = c_iq_i^\top q_i = c_i$$

A fourier series is to break some $f: [0, 2\pi) \rightarrow \mathbb R$ into
$$f(x) = a_0 + a_1 \cos x + b_1 \sin x + a_2 \cos 2x + b_2 \sin 2x + \cdots$$

The key that this is related to linear algebra is we are actually doing some linear combinations under the vector space spanned by the basis $\{1, \sin x, \cos x, \sin 2x, \cos 2x, \cdots\}$.  

If we can find some orthonormal basis, then decomposing $f$ into Fourier Series can be easily found. But first we need to define dot product. The most similar we can do is
$$f \cdot g = \int_0^{2\pi}f(x)g(x) dx$$
This definition leads to many convenient properties:
$$\begin{align*}
\int_0^{2\pi}\sin ax \cos bx dx 
& = \int_0^{2\pi}\frac 1 2\left(\sin (a+b)x+\sin (a-b)x\right) dx \\
& = \int_0^{2(a+b)\pi}\frac{1}{2(a+b)}\sin x dx + \int_0^{2(a-b)\pi}\frac{1}{2(a-b)}\sin x dx \\
& = 0\end{align*}$$

$$\int_0^{2\pi}\sin ax \sin bx dx 
= \int_0^{2\pi}\frac 1 2\left(\cos (a-b)x-\cos (a+b)x\right) dx  
= \begin{cases} \pi & \text{if } a = b \\ 0 & \text{otherwise}\end{cases}$$

$$\int_0^{2\pi}\cos ax \cos bx dx 
= \int_0^{2\pi}\frac 1 2\left(\cos (a+b)x+\cos (a-b)x\right) dx  
= \begin{cases} \pi & \text{if } a = b \\ 0 & \text{otherwise}\end{cases}$$

Therefore, we know that the orthonormal basis is
$$\frac{1}{\sqrt{2\pi}}, \frac{\cos x}{\sqrt{\pi}}, \frac{\sin x}{\sqrt{\pi}}, \frac{\cos 2x}{\sqrt{\pi}}, \frac{\sin 2x}{\sqrt{\pi}}, \cdots$$
and the coefficients are
$$a_0 = \frac{1}{2\pi}\int_0^{2\pi}f(x)dx$$
$$a_n = \frac{1}{\pi}\int_0^{2\pi}f(x)\cos nx dx$$
$$b_n = \frac{1}{\pi}\int_0^{2\pi}f(x)\sin nx dx$$

\[Lecture 18 starts here]

## Determinant

For every **square** matrix $A$, we denote its **determinant** as $\det A$ or $|A|$.  

There are 11 basic properties of determinant, and the first four of them (is one way to) give the explicit definition of determinant.  

1. $\det I = 1$.  
2. Exchanging two different rows of $A$ multiplies its determinant by $-1$. 
   > It is not clear that every *permuting* operation gives the same $\pm 1$ by any swap order, but in fact we have this property:  
   > Define *inversions of a permutation* be the number such that $i < j$ but $p_i > p_j$, then whenever we swap two different elements, the parity of number of inversions changes.  
   > Therefore if we think it as the parity of inversions, every permuting operation gives $\pm 1$ no matter how one performs the swap.  
3. Multipling a row by $c$ multiplies its determinant by $c$.  
4. If two matrices $A, B$ only differ by 1 row, then matrix $C$ obtained by copying other rows but adding up the different row has $\det C = \det A + \det B$.  
5. If matrix $A$ has two same row then $\det A = 0$.  
   *Proof.* If we swap the two rows, we have $\det A = -\det A \Rightarrow \det A = 0$.  
6. Subtracting $c$ times row $i$ to row $j$ (with $i \neq j$) does not change the determinant.  
   *Proof.* According to 4. we can break the row apart, and extract $-c$ from the matrix conatining the subtract operation, which gives determinant $0$. Therefore the determinant does not change.  
7. If matrix $A$ has a row of zero then $\det A = 0$.  
   *Proof.* We add any row to the zero row, and according to 5., $\det A = 0$.  
8. For some upper-triangular matrix $A$ with $d_1, d_2, \cdots, d_n$ on its main diagonal, then $\det A = \prod d_i$.  
   *Proof.* According to 6. we can eliminate all elements not on the main diagonal, therefore we can compute that according to 3.  
   The same holds for lower-triangular, so an efficient way to compute determinant is by $LU$-decomposition and calculating the determainant by multiplying numbers on the diagonal.  
9. $\det A = 0$ if $A$ is singular; $\det A \neq 0$ if $A$ is invertible.  
   *Proof.* With 6. we can do elimination and this property is pretty obvious.  
10. $\det AB = \det A \det B$.
11. $\det A^\top  = \det A$.
    *Proof.* If $A$ is singular then both sides are $0$. Otherwise let $A = LU$, then $A^\top =U^\top L^\top $ and it is obvious that $\det A^\top  = \det U^\top  \det L^\top  = \det U \det L = \det L \det U = \det A$.  

\[Lecture 19 starts here]

### The Big Formula
From property 4, we can break the matrix into multiple parts:
$$\begin{vmatrix} a & b \\ c & d \end{vmatrix} = \begin{vmatrix} a & 0 \\ c & d \end{vmatrix} + \begin{vmatrix} 0 & b \\ c & d \end{vmatrix} = \begin{vmatrix} a & 0 \\ c & 0 \end{vmatrix} + \begin{vmatrix} a & 0 \\ 0 & d \end{vmatrix} + \begin{vmatrix} 0 & b \\ c & 0 \end{vmatrix} + \begin{vmatrix} 0 & b \\ 0 & d \end{vmatrix} = \begin{vmatrix} a & 0 \\ 0 & d \end{vmatrix} + \begin{vmatrix} 0 & b \\ c & 0 \end{vmatrix} \\ = ad - bc$$
There will be $n^n$ parts, but only those with non-zero columns will give a non-zero determinant, therefore we are left with $n!$ parts. In $3 \times 3$,
$$\begin{align*}
& \begin{vmatrix} 
	a_{1, 1} & a_{1, 2} & a_{1, 3} \\ 
	a_{2, 1} & a_{2, 2} & a_{2, 3} \\ 
	a_{3, 1} & a_{3, 2} & a_{3, 3} 
\end{vmatrix} \\
= & \begin{vmatrix} 
	a_{1, 1} & 0 & 0 \\ 
	0 & a_{2, 2} & 0 \\ 
	0 & 0 & a_{3, 3} 
\end{vmatrix} - \begin{vmatrix} 
	a_{1, 1} & 0 & 0 \\ 
	0 & 0 & a_{2, 3} \\ 
	0 & a_{3, 2} & 0 
\end{vmatrix} - \begin{vmatrix} 
	0 & a_{1, 2} & 0 \\ 
	a_{2, 1} & 0 & 0 \\ 
	0 & 0 & a_{3, 3} 
\end{vmatrix} \\
+ & \begin{vmatrix} 
	0 & a_{1, 2} & 0 \\ 
	0 & 0 & a_{2, 3} \\ 
	a_{3, 1} & 0 & 0
\end{vmatrix} + \begin{vmatrix} 
	0 & 0 & a_{1, 3} \\ 
	a_{2, 1} & 0 & 0 \\ 
	0 & a_{3, 2} & 0
\end{vmatrix} - \begin{vmatrix} 
	0 & 0 & a_{1, 3} \\ 
	0 & a_{2, 2} & 0 \\ 
	a_{3, 1} & 0 & 0 
\end{vmatrix}
\end{align*}$$

We can obtain the general formula by
$$\det A_{n\times n} = \sum_{\text{permutation p}}\mathrm{sgn}(p)a_{1,p_1}a_{2,p_2}\cdots a_{n,p_n}$$

### Cofactors
There is a way to simplify the matrix. Take $3\times 3$ as an example:
$$\begin{align*}
& \begin{vmatrix} 
	a_{1, 1} & a_{1, 2} & a_{1, 3} \\ 
	a_{2, 1} & a_{2, 2} & a_{2, 3} \\ 
	a_{3, 1} & a_{3, 2} & a_{3, 3} 
\end{vmatrix} \\
= & \begin{vmatrix} 
	a_{1, 1} & 0 & 0 \\ 
	0 & a_{2, 2} & 0 \\ 
	0 & 0 & a_{3, 3} 
\end{vmatrix} - \begin{vmatrix} 
	a_{1, 1} & 0 & 0 \\ 
	0 & 0 & a_{2, 3} \\ 
	0 & a_{3, 2} & 0 
\end{vmatrix} - \begin{vmatrix} 
	0 & a_{1, 2} & 0 \\ 
	a_{2, 1} & 0 & 0 \\ 
	0 & 0 & a_{3, 3} 
\end{vmatrix} \\
+ & \begin{vmatrix} 
	0 & a_{1, 2} & 0 \\ 
	0 & 0 & a_{2, 3} \\ 
	a_{3, 1} & 0 & 0
\end{vmatrix} + \begin{vmatrix} 
	0 & 0 & a_{1, 3} \\ 
	a_{2, 1} & 0 & 0 \\ 
	0 & a_{3, 2} & 0
\end{vmatrix} - \begin{vmatrix} 
	0 & 0 & a_{1, 3} \\ 
	0 & a_{2, 2} & 0 \\ 
	a_{3, 1} & 0 & 0 
\end{vmatrix} \\
= & +a_{1,1}\left(\begin{vmatrix} 
	1 & 0 & 0 \\ 
	0 & a_{2, 2} & 0 \\ 
	0 & 0 & a_{3, 3} 
\end{vmatrix} - \begin{vmatrix} 
	1 & 0 & 0 \\ 
	0 & 0 & a_{2, 3} \\ 
	0 & a_{3, 2} & 0 
\end{vmatrix}\right) \\
& +a_{1, 2}\left(\begin{vmatrix} 
	0 & 1 & 0 \\ 
	a_{2, 1} & 0 & 0 \\ 
	0 & 0 & a_{3, 3}
\end{vmatrix} - \begin{vmatrix} 
	0 & 1 & 0 \\ 
	0 & 0 & a_{2, 3} \\ 
	a_{3, 1} & 0 & 0
\end{vmatrix}\right) \\
& +a_{1, 3}\left(\begin{vmatrix} 
	0 & 0 & 1 \\ 
	a_{2, 1} & 0 & 0 \\ 
	0 & a_{3, 2} & 0
\end{vmatrix} - \begin{vmatrix} 
	0 & 0 & 1 \\ 
	0 & a_{2, 2} & 0 \\ 
	a_{3, 1} & 0 & 0 
\end{vmatrix}\right) \\
= & +a_{1,1}\left(\begin{vmatrix} 
	a_{2, 2} & 0 \\ 
	0 & a_{3, 3} 
\end{vmatrix} - \begin{vmatrix} 
	0 & a_{2, 3} \\ 
	a_{3, 2} & 0 
\end{vmatrix}\right) \\
&-a_{1, 2}\left(\begin{vmatrix}
	a_{2, 1} & 0 \\ 
	0 & a_{3, 3}
\end{vmatrix} - \begin{vmatrix}
	0 & a_{2, 3} \\ 
	a_{3, 1} & 0
\end{vmatrix}\right) \\
&+a_{1, 3}\left(\begin{vmatrix} 
	a_{2, 1} & 0 \\ 
	0 & a_{3, 2} 
\end{vmatrix} - \begin{vmatrix}
	0 & a_{2, 2} \\ 
	a_{3, 1} & 0 
\end{vmatrix}\right)
\end{align*}$$

Let $M_{a, b}$ is the matrix obtained by erasing row $a$ and column $b$ from $A$.   
We can rewrite the big formula of $n\times n$ matrix to this:
$$\det A_{n\times n} = \sum_{i=1}^{n}a_{1, i}(-1)^{i+1}\det M_{1, i} = \sum_{i=1}^{n}a_{1, i}$$

Moreover, instead of expanding by row $1$, we can do that for any row $i$:
$$\det A_{n\times n} = \sum_{j=1}^{n}a_{i, j}(-1)^{i+j}\det M_{i, j}$$
> The reason the sign is $(-1)^{i+j}$ is actually *how the parity of inversion will change if we insert $i$ into position $j$*.  
> Assume there are $k$ numbers that are greater than $i$ in position $1$ to $j - 1$, then the inversion is going to increase by
> $$k + (n - j) - (n - i - k) = i - j$$
> and it is equivlant to $i + j$ modulo $2$.  

This formula is useful for some matrices where most of one row is zero. For example the tridiagonal matrix:
$$A_n = \left[a_{i, j} = \begin{cases} 1 & \text{if } |i - j| \leq 1 \\ 0 & \text{otherwise}\end{cases}\right]_{n\times n}$$
We have
$$\det A_1 = |1| = 1, \det A_2 = \begin{vmatrix} 1 & 1 \\ 1 & 1 \end{vmatrix} = 0$$
$$A_n = 
\begin{bmatrix} 
	1 & 1 & 0 & \cdots & 0 \\
	1 & 1 & 1 & \cdots & 0 \\
	0 & 1 \\
	\vdots & \vdots & & A_{n-2} \\
	0 & 0\\
\end{bmatrix}$$
$$\det A_n = \det A_{n - 1} - \det A_{n - 2}$$

\[Lecture 20 starts here]

### Inverse Formula
Let the cofactor matrix $C$ be $c_{i, j} = (-1)^{i + 1}\det M_{i, j}$.  
The inverse of $A$ is 
$$A^{-1} = \frac 1 {\det A}C^\top $$
Why?
For the main diagaonal of row $i$,
$$\sum_{j = 1}^{n}a_{i, j}c_{i, j} = \det A$$
For the rest, say row $i$ column $j$,
$$\sum_{k=1}^{n}a_{i, k}c_{j, k}$$
we rebuild a matrix $K$ the same with $A$ but the row $j$ is replaced by row $i$, then this matrix is singular and $\det K = 0$.  
Therefore $AC^\top  = (\det A)I$, $A^{-1} = \frac 1 {\det A}C^\top $.  

### Cramer's Rule
If $A$ is invertible then
$$Ax = b \Rightarrow x = A^{-1}b = \frac 1 {\det A} C^\top b$$
What is $x_i$?
$$x_i = \frac 1 {\det A}\sum_{j=1}^n b_jc_{j, i}$$
If we define the matrix $B_i$ the same with $A$ but the column $i$ is replaced by $b$, then
$$x_i = \frac{\det B_i}{\det A}$$
In general, Cramer's rule is a disastrous mess (since determinant computation is awful, the best way to do that is probably elimination). However it sure has some value, for example this is the *algebraic* form of the solution instead of doing some algorithms.  

### Volumes
**Property.** The volume defined by the $n$ row vectors of $A$ is $|\det A|$.  
*Proof.*  
1. $\det I = 1$ and the volume defined by these vector is indeed $1$.
2. By definition, it is true.  
3. If we stretch any vector by scalar $c$, the volume multiplies by $|c|$.  
4. Assume the two vector are $u$ and $v$, let the rest vector form the base, then we are going to consider the height (i.e. the projection error $e$), and this projection is linear so the same property holds for both determinant and volume.  

Another way to see this is directly by Gram-Schmidt process. The volume defined by these orthogonal vectors are intuitive.  

*Special Case.* The signed area of triangle with corners $(x_1, y_1), (x_2, y_2), (x_3, y_3)$ is 
$$\frac 1 2\begin{vmatrix}x_1 & y_1 & 1 \\ x_2 & y_2 & 1 \\ x_3 & y_3 & 1 \end{vmatrix}$$

\[Lecture 21 starts here]

## Eigenvalues and Eigenvectors
**Definition.** The **eigenvectors** of a square matrix $A$ is the non-zero vectors satisfying
$$Ax = \lambda x$$
for some $\lambda$. Here, $\lambda$ is called the **eigenvalue**.  

We don't know anything about that, but here is a cool thing:
$$Ax = \lambda x\Rightarrow (A - \lambda I)x = 0 \Rightarrow \det (A - \lambda I) = 0$$
Let's see some instances of eigenvalues and eigenvectors.  

For projection matrix $P$, if $x$ is aleady in the column space $C(A)$ then $Px = x$ and $x$ is an eigenvector with $\lambda = 1$; if $x$ is perpendicular to $C(A)$ then $Px = \mathbf 0$ and $x$ is an eignenvector with $\lambda = 0$.  

For $A = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$, we have $x_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}, \lambda_1 = 1$ and $x_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}, \lambda_1 = -1$.  

For $A = \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}$, 
$$A - \lambda I = \begin{bmatrix} 3 - \lambda & 1 \\ 1 & 3 - \lambda \end{bmatrix} \Rightarrow (3 - \lambda)^2 - 1 = 0 \Rightarrow \lambda_1 = 2, \lambda_2 = 4$$
$x_1$ is in $N(A - 2I) \Rightarrow x_1 = \begin{bmatrix}1 \\ 1\end{bmatrix}$, $x_2$ is in $N(A - 4I) \Rightarrow x_2 = \begin{bmatrix}1 \\ -1\end{bmatrix}$.

For $A = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ which rotates any vector by 90 degree counterclockwise, things are getting strange: what the hell vector is going to have the same direction when rotated by 90 degree?  
$$A - \lambda I = \begin{bmatrix} -\lambda & -1 \\ 1 & -\lambda \end{bmatrix} \Rightarrow \lambda^2 + 1 = 0 \Rightarrow \lambda = i, -i$$
WHAT?  
It turns out the eigenvalues can be *complex* even when $A$ is a real value matrix.  
> This is why the lecturer told "it was a disaster" since imaginary numbers were not invented until 1804.  

For $A = \begin{bmatrix} 3 & 1 \\ 0 & 3 \end{bmatrix}$,
$$A - \lambda I = \begin{bmatrix} 3 - \lambda & 1 \\ 0 & 3 - \lambda \end{bmatrix} \Rightarrow (3 - \lambda)^2 = 0 \Rightarrow \lambda_1 = \lambda_2 = 3$$
but the thing is there is only one eigenvector: $x = \begin{bmatrix}1 \\ 0\end{bmatrix}$.

It is noteworthy that eigenvalues are **not additive (linear) and multiplicative**. Eigenvalues of $A, B$ 
have nothing to do with eigenvalues of $A+B, AB$.  

\[Lecture 22 starts here]

### Diagonalization

Suppose we have $n$ linearly independent eigenvectors of $A$, we put them in the columns of $S$,
$$AS = \begin{bmatrix}\lambda_1x_1 & \lambda_2x_2 & \cdots & \lambda_nx_n\end{bmatrix} = 
\underbrace{\begin{bmatrix}
	\lambda_1 & 0 & \cdots & 0 \\ 
	0 & \lambda_2 & \cdots & 0 \\
	\vdots & \vdots & \ddots & \vdots \\  
	0 & 0 & \cdots & \lambda_nx_n
\end{bmatrix}}_\Lambda S$$
If $S$ is invertible (if there are linearly indepenent, under our assumption), then we can write
$$A = S^{-1}\Lambda S$$

> ### Trace and determinant
> This part is only mentioned in the lectures but not deeply discussed, this part is meant to fill in that.  
>
> **Theorem.** The sum of all eigenvalues is equal the *trace* of $A$, which is the sum of the main diagonal.  
> *Proof.* We take a look on the characteristic polynomal of matrix $A$, we want to show that
> $$t^n - \mathrm{tr}(A) t^{n - 1} + \underbrace{\cdots}_{\text{terms under }t^{n-2}} = 0$$
> Consider $A - tI$, for $n = 1$, the above equation holds.  
> Suppose all matrices with $n \leq k$ holds, for any matrix that is $(k+1)\times(k+1)$, we have
> $$\begin{align*}
 \det (A - tI) & = 
 \det \begin{bmatrix}
 	a_{1, 1} - t & a_{1, 2} & \cdots & a_{1, n} \\ 
 	a_{2, 1} & a_{2, 2} - t & \cdots & a_{2, n} \\
 	\vdots & \vdots & \ddots & \vdots \\
 	a_{n, 1} & a_{n, 2} & \cdots & a_{n, n} - t\\
 \end{bmatrix} \\
 & = \det \begin{bmatrix}
 	- t & 0 & \cdots & 0 \\ 
 	a_{2, 1} &  & \cdots &  \\
 	\vdots & \vdots & \ddots & \vdots \\
 	a_{n, 1} &  & \cdots & \\
 \end{bmatrix} + \det \begin{bmatrix}
 	a_{1, 1} & a_{1, 2} & \cdots & a_{1, n} \\ 
 	a_{2, 1} &  & \cdots &  \\
 	\vdots & \vdots & \ddots & \vdots \\
 	a_{n, 1} &  & \cdots & \\
 \end{bmatrix} \\
 \end{align*}$$
> We want to keep the terms which have $t^{n-1}$. In the second matrix, the only way is to have $a_{1, 1}$. Because otherwise if we have $a_{1, i}$, then for the rest $n - 1$ of $t$s we can only choose maximum $n - 2$ of them.  
> Therefore we are only interested in
> $$\begin{align*}
 & (a_{1, 1} - t) \det \begin{bmatrix}
 	a_{2, 2} - t & \cdots & a_{2, n} \\
 	\vdots & \ddots & \vdots \\
 	a_{2, n} & \cdots & a_{n, n} - t \\ 
 \end{bmatrix} \\
 = & (a_{1, 1} - t)(t^{n-1} - (a_{2,2} + a_{3,3}+\cdots+a_{n,n})t^{n - 2} + \cdots) \\
 = & (-1)(t^n - (a_{1,1} + a_{2,2} + a_{3,3}+\cdots+a_{n,n})t^{n - 1} + \cdots)
 \end{align*}$$
> which is what we desired.  
> By math induction all finite square matrices have this property.  
>
> **Theorem.** The product of all eigenvalues is equal the *determinant* of $A$.  
> *Proof.* Now we are interested in the last term of the charateristic polynomial:
> $$t^n + \underbrace{\cdots}_{\text{terms having }t} + (-1)^n\det A = 0$$
> We can do the expand thing we have just done, but instead we drop all the terms having $t$, and we are left with $\det A$.  

### $A$ powered
Suppose $Ax = \lambda x$, then for $A^2$,  
$$A^2x = A\lambda x = \lambda^2x$$
Same holds for the diagonalization we just have:
$$A^2 = S^{-1}\Lambda S S^{-1}\Lambda S = S^{-1}\Lambda^2 S$$

In fact we can do this *any integer times*, therefore
$$A^kx = \lambda^kx$$
$$A^k = S^{-1}\Lambda^k S$$

**Theorem.** $\lim_{k \rightarrow \infty} A = \mathbf 0$ if all $|\lambda_i| < 1$.  

When can we do such convenient thing? It turns out  
**Property.** $A$ is sure to have $n$ independent eigenvectors if all eigenvalues are different.  
> *Proof.*
> If we have only one vector $x_1$, then $x_1$ is sure to be linearly independent.  
> Assume we already have $k - 1$ linearly independent eigenvectors, then consider the $k$-th eigenvector.  
> We want to show that
> $c_1x_1 + c_2x_2 + \cdots + c_kx_k$ only have a solution of $c_i = 0$.  
> Let $c = \begin{bmatrix}c_1, c_2, \cdots, c_k, 0, \cdots, 0\end{bmatrix}$. The equation is equivlant to
> $$Sc = \mathbf 0$$
> Multiply both side by $A$ gives
> $$ASc = S\Lambda c = \mathbf 0$$
> Therefore if $c$ is a solution, then $\Lambda c$ is also a solution, which means  
> $$\begin{cases}c_1x_1 + c_2x_2 + \cdots + c_kx_k = \mathbf 0 \\ c_1\lambda_1x_1 + c_2\lambda_2x_2 + \cdots + c_k\lambda_kx_k = \mathbf 0\end{cases}$$
> Multiply the first equation by $\lambda_k$ we get
> $$c_1(\lambda_1-\lambda_k)x_1 + c_2(\lambda_2-\lambda_k)x_2 + \cdots + c_{k-1}(\lambda_{k-1}-\lambda_k)x_{k-1} = \mathbf 0$$
> If $c$ is non-zero, then $c_1, \cdots, c_k$ has at least two non-zero entries. Because all $\lambda_i$ are different, at least one $c_i(\lambda_i - \lambda_k)$ is non-zero.  
> However by induction hypothesis, $x_1, \cdots, x_{k-1}$ are linearly independent so $c_1, \cdots, c_{k-1}$ must be all zero.  
> We have met a contradiction and thus, there is no solution $c$ other than zero and $x_1, \cdots, x_k$ are thus linearly independent.  
> By math induction, all eigenvectors are linear independent if their eigenvalues are different.   

#### Solving $A$ powered
Suppose we have some column vector $u_0$ and recursively $u_{k+1} = Au_k$. How do we found $u_k$?  

Let's say $u_0 = c_1x_1 + c_2x_2 + \cdots + c_nx_n = Sc$,  
then $u_1 = c_1\lambda_1x_1 + c_2\lambda_2x_2 + \cdots + c_n\lambda_nx_n = S\Lambda c$.  
Furthurmore, $u_k = c_1\lambda_1^kx_1 + c_2\lambda_2^kx_2 + \cdots + c_n\lambda_n^kx_n = S\Lambda^kc$.  
> In fact it is simply $u_k = S\Lambda^kS^{-1}u_0$.  

For example we have Fibonacci sequence:
$$\begin{cases}F_0 = 0 \\ F_1 = 1 \\ F_{n+2} = F_{n+1} + F_n\end{cases}$$
and we can build it as
$$\underbrace{\begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}}_A\begin{bmatrix} F_{n+1} \\ F_{n} \end{bmatrix} = \begin{bmatrix} F_{n+2} \\ F_{n+1} \end{bmatrix}$$
Solving it:
$$\det (A - \lambda I) = \begin{vmatrix} 1 - \lambda & 1 \\ 1 & - \lambda \end{vmatrix} \Rightarrow \lambda^2 - \lambda - 1 = 0 \Rightarrow \lambda_1 = \frac{1 + \sqrt 5}{2}, \lambda_2 = \frac{1 - \sqrt 5}{2}$$
Finding null space of $A - \lambda I$:  
Since this matrix has a special property of $(\lambda - 1)\lambda = 1$,  
$$x_1 = \begin{bmatrix} \lambda_1 \\ 1 \end{bmatrix}, x_2 = \begin{bmatrix} \lambda_2 \\ 1 \end{bmatrix}$$
and
$$\begin{bmatrix} 1 \\ 0 \end{bmatrix} = \frac{x_1 - x_2}{\lambda_1 - \lambda_2} $$
We have
$$\begin{bmatrix} F_{n+1} \\ F_{n} \end{bmatrix} = A^n\begin{bmatrix} 1 \\ 0 \end{bmatrix} = \frac{\lambda_1^nx_1 - \lambda_2^nx_2}{\lambda_1 - \lambda_2} $$
$$F_n = \frac{\lambda_1^n - \lambda_2^n}{\lambda_1 - \lambda_2} = \frac{1}{\sqrt 5}\left(\left(\frac{1 + \sqrt 5}{2}\right)^n-\left(\frac{1 - \sqrt 5}{2}\right)^n\right) \approx \frac{1}{\sqrt 5}\left(\frac{1 + \sqrt 5}{2}\right)^n$$

\[Lecture 23 starts here]

### Differential Equations
In this part we are interested in systems look like this:
$$\begin{cases}\begin{matrix}
\dfrac{du_1}{dt} & = & a_{1,1}u_1 & + &a_{1,2}u_2 & + &\cdots & + & a_{1,n}u_n \\
\dfrac{du_2}{dt} & = & a_{2,1}u_1 & + &a_{2,2}u_2 & + &\cdots & + & a_{2,n}u_n \\
\vdots & = & \vdots & + & \vdots & + &\ddots & + &\vdots \\
\dfrac{du_n}{dt} & = & a_{n,1}u_1 & + &a_{n,2}u_2 & + &\cdots & + & a_{n,n}u_n \\
\end{matrix}\end{cases}$$
Which can be write as
$$\frac{d\mathbf u}{dt} = A\mathbf u$$
The special solution to this is
$$\mathbf u = e^{\lambda_it}x_i$$
since
$$\frac{d\mathbf u}{dt} = \lambda_ie^{\lambda_it}x_i = A\mathbf u$$

Therefore we can solve these as
$$\mathbf u = c_1e^{\lambda_1t}x_1 + c_2e^{\lambda_2t}x_2 + \cdots + c_ne^{\lambda_nt}x_n$$

Given some $\mathbf u(t_0)$, we can do some elimination to obtain $\mathbf u$.  
There are some interesting property of *every* $\mathbf u$:
1. Stability. $\lim_{t \rightarrow \infty} \mathbf u(0) = \mathbf 0$ if $\textrm{Re}(\lambda_i) \leq 0$.  
   The imaginary part does not matter since $e^{i\theta} = \cos \theta + i \sin \theta$ and it always have the modular of $1$.  
2. Steady state. $\frac{d\mathbf u}{dt} = \mathbf u$ if some $\lambda_i = 0$ and others have $\textrm{Re}(\lambda_i) \leq 0$.  
3. Blow up. If any $\textrm{Re}(\lambda_i) > 0$.  

Notes on $2$ variable differential equation: for matrix $A = \begin{vmatrix}a & b \\ c & d \end{vmatrix}$, we can verify this matrix is stable or blowing up by $a + d < 0$ and $ad - bc > 0$.  

We can do more things than we current have.  
Let's say $A$ has $n$ independent eigenvectors, and for the vector function $u$, we find
$$S\mathbf u = \mathbf v$$
then
$$S\frac{d\mathbf v}{dt} = AS\mathbf v$$
$$\frac{d\mathbf v}{dt} = \Lambda\mathbf v$$
We are going to write that as
$$\mathbf v(t) = e^{\Lambda t}\mathbf v(0), \mathbf u(t) = Se^{\Lambda t}S^{-1}\mathbf u(0) = e^{A t}\mathbf u(0)$$
Wait a minute, what is $e^{At}$? 

**Definition.** We define $e^{A}$ by the Taylor Series:
$$e^A = I + A + \frac{A^2}{2!} + \frac{A^3}{3!} + \cdots = \sum_{n = 0}^{\infty}\frac{A^n}{n!}$$

It is clear that
$$e^{At} = \sum_{n = 0}^{\infty}\frac{A^nt^n}{n!} = \sum_{n = 0}^{\infty}\frac{S\Lambda^nS^{-1}t^n}{n!} = S\sum_{n = 0}^{\infty}\frac{\Lambda^nt^n}{n!}S^{-1} = Se^{\Lambda t}S^{-1}$$
if $A$ is diagonalizable.  

### Ordinary Differential Equation
Let's start with order $2$:
$$y'' + by' + ky = 0$$
Setup a column vector by
$$u = \begin{bmatrix} y' \\ y\end{bmatrix}$$
then
$$u' = \begin{bmatrix} y'' \\ y'\end{bmatrix}$$
and we have
$$\begin{bmatrix} y'' \\ y'\end{bmatrix} = \begin{bmatrix}
-b & -k \\
1 & 0 \\\end{bmatrix}\begin{bmatrix} y' \\ y\end{bmatrix}$$
which is solving 
$$\frac{du}{dx} = Au$$

In fact, every ordinary differential equation with order $n$ can be solved by setting

$$\begin{bmatrix} y^{(n)} \\ \vdots \\ y'\end{bmatrix} = \begin{bmatrix}
-a_{n-1} & -a_{n-2} & -a_{n-3} & \cdots & -a_1 \\
1 & 0 & \cdots & \cdots & 0 \\
0 & 1 & 0 & \cdots & 0 \\
\vdots & \vdots & \ddots & \ddots & \vdots\\
0 & 0 & \cdots & 1 & 0\\\end{bmatrix}\begin{bmatrix} y^{(n-1)} \\ \vdots \\ y\end{bmatrix}$$

and use the technique mentioned on previous section.  

\[Lecture 24 starts here]
### Markov Matrix
**Definition.** A markov matrix is a matrix that satisfies  
1. $0 \leq a_{i, j}$  
2. $\sum_{i = 0}^{n}a_{i, j} = 1$  

**Property.** Any markov matrix $A$ has a eigenvalue of $\lambda = 1$.  
*Proof.* Considering $A - I$ has all columns sum to $0$, it is not a full row rank matrix so it is singular and $\det (A - I) = 0$.   

**Property.** Any markov matrix $A$ has all eigenvalues $|\lambda_i| \leq 1$.  
> *Proof.* Let $\lambda$ be any eigenvalue of $A$, we have
> $$Ax = \lambda x$$
> Therefore
> $$|\lambda|\sum_{i=1}^{n}|x_i| = \sum_{i=1}^{n}\left|\sum_{j=1}^{n}a_{i, j}x_j\right| \leq \sum_{i=1}^{n}\sum_{j=1}^{n}|a_{i, j}||x_j| = \sum_{i=1}^{n}\sum_{j=1}^{n}a_{i, j}|x_j| = \sum_{i=1}^{n}|x_i|$$
> Therefore $|\lambda| \leq 1$.  

By this property, we know for some initial $u_0$, when $A^ku_0$ converges as $k \rightarrow \infty$, the parts with $|\lambda| < 1$ decay and left with all the steady states.  

The way to find all steady states (i.e. $Ax = x$) is by finding the null space of $A - I$.  

\[Lecture 25 starts here]

### Symmetric Matrices
Let $A$ be a symmetric matrix.  

**Property.** All eigenvalues $\lambda_i$ of $A$ is real.  
*Proof.* Assume $x$ is the correspond eigenvector of eigenvector $\lambda$.  
$$Ax = \lambda x \Rightarrow \bar A\bar x = \bar\lambda \bar x \Rightarrow \bar x^\top \bar A = \bar\lambda \bar x^\top $$
Let $A^*$ be the conjugate transpose of $A$.  
We have
$$x^*A = \bar \lambda x^* \Rightarrow x^*Ax = \lambda x^*x = \bar \lambda x^*x$$
Since $x$ is non-zero, $\|x\|^2 = x^*x > 0$, and $\lambda = \bar\lambda \Rightarrow \lambda \in \mathbb R$.  

**Property.** We can choose $n$ orthonormal eigenvectors of $A$.  
> *Proof.* We introduce a more general case: The Spectral Theorem.  
> Link: [https://math.mit.edu/~dav/spectral.pdf](https://math.mit.edu/~dav/spectral.pdf)
> For now this part is skipped and it will be filled in later (hope so).  

Using the two properties we get that not only $A$ is diagonalizable but also  
$$A = Q\Lambda Q^{-1} = Q\Lambda Q^\top $$  
and  
**Proposition.** Every symmetric matrix is a linear combination of projection matrices.  

**Property.** For symmetric matrices, the signs of the pivots are the same as the signs of the eigenvalues.  
> *Proof.* There is a thing called congurent relation, link: https://math.stackexchange.com/questions/57887/how-does-number-of-signs-of-pivots-same-as-number-of-signs-of-eigenvalues-help-i  
> For short, for symmetric matrix $A$ and non-singular matrix $M$, $MAM^\top $ has the same signs of the eigenvalues with $A$.  
> Since the symmetric matrix can have a $LDL^\top$ decomposition, if the abovementioned theorem is true then this property is true then.  

\[Lecture 26 starts here]  

## Complex Matrices  
There are some details we are going to change before we go from *real* to *complex*.  

  - Norm  
	In real world, we can take $|a|^2 = a^2$, but in complex numbers, $|z|^2 = z\bar z$.  
	Therefore the new definition of magnitude is  
	$$\|v\|^2 = v^Hv \quad (v^H = \bar v^\top )$$
	We call the conjugate transpose of $v$ the *Hermitian* of $v$.  
  - Inner Product  
	We are going to change the definition of inner product because this definition is subjective to the definition of norm.  
	$$y \cdot x = y^Hx$$ 
  - Symmetric Matrix  
	Now symmetric matrices are the matrices satisfying  
	$$\bar A^\top  = A^H = A$$
  - Orthogonal  
	A new definition: if complex square matrix $Q$ satisfying  
	$$Q^HQ = I$$
	then $Q$ is called a **unitary** matrix.  

### Fast Fourier Transform  
Motivation: A polynomial of degree $n$ can be multiplied in $\mathcal O(n)$ multiplication if it is in the form of point values. To multiply two polynomial, we are interested in how to *transform* *fast* between terms and point values.  

**Definition.** DFT matrix $F_n = [\omega_n^{(i-1)(j-1)}]_{n\times n}$. Here, $\omega_n = e^{\frac{2\pi i}{n}} = \cos \frac{2\pi}{n} + i \sin \frac{2\pi}{n}$.   
For example, 
$$F_4 = 
\begin{bmatrix} 
	1 & 1 & 1 & 1 \\
	1 & i & i^2 & i^3 \\
	1 & i^2 & i^4 & i^6 \\
	1 & i^3 & i^6 & i^9
\end{bmatrix} = \begin{bmatrix} 
	1 & 1 & 1 & 1 \\
	1 & i & -1 & -i \\
	1 & -1 & 1 & -1 \\
	1 & -i & -1 & i
\end{bmatrix}$$

**Property.** $F_n$ is symmetric and the columns are orthogonal.  

Consider the odd columns and even columns separately:
To generate these columns,   
$$\begin{bmatrix} 
	1 & 1 \\
	1 & (i^2) \\
	1 & (i^2)^2 \\
	1 & (i^2)^3
\end{bmatrix} = \begin{bmatrix} 
	1 &  \\
	 & 1 \\ 
	1 &  \\
	 & 1 \\ 
\end{bmatrix}\begin{bmatrix} 
	1 & 1 \\
	1 & -1 \\ 
\end{bmatrix}$$
For the even rows,
$$\begin{bmatrix} 
	1 & 1 \\
	i & i^3 \\
	i^2 & i^6 \\
	i^3 & i^9
\end{bmatrix} = \begin{bmatrix} 
	1 \\
	& i \\
	i^2 \\
	& i^3\\
\end{bmatrix}\begin{bmatrix} 
	1 & 1 \\
	1 & -1 \\ 
\end{bmatrix}$$
Therefore
$$\begin{bmatrix} 
	1 & 1 & 1 & 1 \\
	1 & i^2 & i & i^3 \\
	1 & i^4 & i^2 & i^6 \\
	1 & i^6 & i^3 & i^9
\end{bmatrix} = \begin{bmatrix} 
	1 &  & 1  \\
	 & 1 & & i \\ 
	1 && i^2\\
	& 1 && i^3\\
\end{bmatrix}\begin{bmatrix} 
	1 & 1 \\
	1 & -1 \\
	&& 1 & 1 \\
	&& 1 & -1  \\ 
\end{bmatrix}$$
so 
$$F_4 = \begin{bmatrix} 
	1 &  & 1  \\
	 & 1 & & i \\ 
	1 && i^2\\
	& 1 && i^3\\
\end{bmatrix}\begin{bmatrix} 
	F_2 \\
	& F_2
\end{bmatrix}\begin{bmatrix} 
	1 & & \\
	 & & 1 &  \\ 
	 & 1 &\\
	& & & 1\\
\end{bmatrix}$$

**Property.** 
Let 
$$D_n = \left[\begin{cases} \omega^i & i = j \\ 0 & \text{otherwise}\end{cases}\right]_{n\times n}, P_n = \left[\begin{cases} 1 & i \leq \frac n 2 \text{ and } j = 2i - 1 \\ 1 & i > \frac n 2 \text{ and } j = 2i \\ 0 & \text{otherwise}\end{cases}\right]_{n\times n}$$
 then for any general $F_n$ we can compute it as  
$$F_n = \begin{bmatrix} 
	F_{\frac n 2} \\
	& F_{\frac n 2}
\end{bmatrix}\begin{bmatrix} 
	I & D_{\frac n 2} \\
	I & -D_{\frac n 2} \\
\end{bmatrix}P_n$$  
Utilizing this formula makes multiplication of $F_nx$ takes only $\mathcal O(n \log n)$ of time.  

In fact we have $F_n^HF_n = nI$, so inverse should not be a problem.  

\[Lecture 27 starts here]

### Positive Definite Symmetric Matrices
**Definition.** A Hermitian matrix $A$ is called *positive-definite matrix* if all eigenvalues of $A$ is positive.  
**Theorem.** A Hermitian matrix $A$ is called *positive-definite matrix* is equivlant to all the following properties:
1.  All the pivots are positive.  
2.  All the determinant of the top left $k\times k$ matrices (for $1 \leq k \leq n$) are positive.  
3.  For any non-zero column vector $x$, $x^HAx > 0$.  

> *Proof for 1 $\Leftrightarrow$ 3.* Assume $A$ is a real matrix, if it is not then the proof still works.  
> Let $x = [x_1,x_2,\cdots,x_n]$, then we are finding the minimum of 
> $$f(x_1, x_2, \cdots, x_n) = \sum_{i=1}^{n}a_{i, i}x_i^2 + \sum_{i\neq j}a_{i, j}x_ix_j$$  
> When we do an elimination, we are multiplying the pivot by $-\frac{a_{i, j}}{a_{i, i}}$ and subtract from row $j$, which means for the same $i$, we are doing
> $$\begin{cases}
	a_{j, i} \leftarrow 0 & i < j \\ 
	a_{j,j} \leftarrow a_{j,j} - \frac{a_{i,j}^2}{a_{i,i}} &  \\ 
	a_{j, k} \leftarrow a_{j,k} - \frac{a_{i,j}}{a_{i,i}}a_{j, k} & i \leq j, k \\ 
\end{cases}$$
> We can see the bottom-down submatrix is still Hermitian, so
> $$\begin{align*}
& a_{i, i}x_i^2+\sum\frac{a_{i,j}^2}{a_{i,i}}x_j^2+\sum\frac{a_{i,j}}{a_{i,i}}a_{j, k} \\
= & a_{i, i}x_i^2+\sum\frac{a_{i,j}^2}{a_{i,i}}x_j^2+\sum_{j<k}2\frac{a_{i,j}}{a_{i,i}}a_{j, k} \\
= & a_{i, i}\left(x_i^2+\sum\frac{a_{i,j}^2}{a_{i,i}^2}x_j^2+\sum_{j<k}2\frac{a_{i,j}}{a_{i,i}^2}a_{j, k}\right) \\
= & a_{i, i}\left(x_i+\sum\frac{a_{i,j}}{a_{i,i}}x_j\right)^2 \\
\end{align*}$$
> Therefore the pivots must be positive to make the function positive (you can notice that these vectors in the parathesis must be independent). 
 
**Property.** For any $m \times n$ matrix $A$, $A^\top A$ is semi-positive definite and if its rank is $n$, it is positive definite.  

#### Application
In calculus, for a single variable function $f \in C^2$, $f(x)$ is minmum (maximum) if $f'(x) = 0$ and $f''(x)$ is positive (negative).  
For a multivariable function $f(x_1, x_2, \cdots, x_n)$, $f(\mathbf x)$ is minmum (maximum) if $f_{x_i}(x) = 0$ and the matrix $A = [f_{x_ix_j}(\mathbf x)]_{n\times n}$ is **positive(negative)-definite**.  

#### Ellipsoid
Ellipisoid is a 3D shape looks like a elliptic. A standard ellipisoid has the formula of
$$\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2} = 1$$
For a positive-definite $3\times 3$ matrix, $x^HAx = 1$ is a ellipisoid.  
Since $A$ is Hermitian, we can find $A = Q\Lambda Q^H$, and the equation is
$$x^HQ\Lambda Q^Hx = 1$$
Let $y = Q^Hx$, then we have $y^H\Lambda y = 1$, which is
$$\frac{y_1^2}{\lambda_1}+\frac{y_2^2}{\lambda_2}+\frac{y_3^2}{\lambda_3} = 1$$
That is why we are choosing positive-definite to be the condition.  
Moreover, $\sqrt{\lambda_i}$ is going to be the length of the three axes (treat $Q$ as a linear transform).  

\[Lecture 28 starts here]
## Similar Matrices  
**Definition.** Two square matrices $A$, $B$ are *similar* if there exist a invertible matrix $M$ such that $M^{-1}AM = B$.  

**Property.** Two similar matrices $A, B$ have the same eigenvalues.  
*Proof.*  
$$Ax = \lambda x \Rightarrow M^{-1}AMM^{-1}x =\lambda M^{-1}x \Rightarrow B(M^{-1}x) = \lambda (M^{-1}x)$$

### Jordan Form
**Definition.** A Jordan block $J$ is matrix such that
$$J = \begin{bmatrix}
\lambda & 1 & 0 & \cdots & 0 & 0 \\
0 & \lambda & 1 & \cdots & 0 & 0 \\
0 & 0 & \lambda & \ddots & 0 & 0 \\
\vdots & \vdots & \ddots & \ddots & \ddots & \vdots \\
0 & 0 & 0 & \ddots & \lambda & 1 \\
0 & 0 & 0 & \cdots & 0 & \lambda \\
\end{bmatrix}$$	

**Theorem.** For any square matrix $A$, there exists a matrix $P$ in the form of
$$P = \begin{bmatrix}
J_1 & 0 & 0 & \cdots & 0 \\
0 & J_2 & 0 & \cdots & 0 \\
0 & 0 & J_3 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & J_p \\
\end{bmatrix}$$
where $J_i$ is a Jordan block. Such $P$ is called the **Jordan Canonical Form** of $A$.  

> ### Finding Jordan Canonical Form
> This part does not contain proof currently (since it is said to be hard, but that might be filled up later).  
> For some $n \times n$ square matrix $A$, the problem is that
> $$(A - \lambda I)v = 0$$
> might not have enough solution although $\lambda$ are sure to have $n$ roots of the characteristic polynomial.  
> So we generalize it. A $v$ is called a *generalized eigenvector* if
> $$(A - \lambda I)^kv = 0$$
> for some integer $k$.  
> Then there are always $n$ generalized eigenvectors.
> > *Non-rigorous Proof.*  
> > Assume for some eigenvalue $\lambda$ it has multiplicity $r$ (which means $\lambda$ exists $r$ times as the roots in the characteristic polynomial), then the following equations:
> > $$\begin{cases}(A - \lambda I)v = 0 \\ (A - \lambda I)^2v = 0 \\ \vdots \\ (A - \lambda I)^rv = 0\end{cases}$$
> > solve $r$ linearly independent $v$.
> > Since we can rewrite that as 
> > $$\begin{cases}(A - \lambda I)v_1 = 0 \\ (A - \lambda I)v_2 = v_1 \\ \vdots \\ (A - \lambda I)v_r = v_{r-1}\end{cases}$$
> > $v_{i+1}$ is in $v_i$ equation's row space, and row space is orthogonal to the null space so they should be linearly independent.  
>
> Finding the $n$ generalized eigenvectors follows the procedure below:  
> For each $\lambda_i$ with multiplicity $r$, we solve $(A - \lambda_iI)v = 0$ and see if there is $r$ inearly independent solutions.  
> If not, we solve $(A - \lambda_iI)^2v = 0$, $(A - \lambda_iI)^3v = 0$, and so on until we have $r$ linearly independent solutions.  
> Now we consider the *chain* generated by solving $(A - \lambda_iI)v_{i+1} = v_i$, we can partition these solutions into many chains $\{v_1, v_2, \cdots\}$.  
> Let the chains' sizes be $s_1, s_2, \cdots, s_k$ (there should be $\mathrm{rank}(A - \lambda_iI)$ chains), then the Jordan blocks of $\lambda_i$ has sizes of $s_1, s_2, \cdots, s_k$.  
> (For the proof of why, search Jordan chains and I might fill up this as well later.)  
> 
> Solving each eigenvalues and put their blocks into a matrix gives the Jordan form.  
>
> To find such $M^{-1}AM = P$, we have to find these basis (in the order of *chains*), and put them in the blocks' order first and the decreasing rank order next in $M$.  

The idea for the Jordan Form is because there are some matrices that are not diagonalizable, but by finding the Jordan Form of them, we can obtain a somewhat silimar form. As you can see:

$$A = Q\Lambda Q^{-1}$$
$$A = MPM^{-1}$$

are *similar* to each other.  

\[Lecture 29 starts here]

## Single Value Decomposition
The target of single value decomposition is to decompose **ANY** $m \times n$ matrix $A$ into
$$A = U\Sigma V^\top$$
where $U, V$ are orthogonal matrices and $\Sigma$ is a diagonal matrix.  

It is equivlant to
$$AV = U\Sigma$$
which means we are going to find orthonormal basis $v_i$ in row space, and $\sigma_i u_i = Av_i$ is an orthogonal basis of the column space.  

How do we find it? A cool identity is
$$A^\top A = V\Sigma^\top U^\top U\Sigma V^\top = V\begin{bmatrix}\sigma_1 \\ & \sigma_2 \\ && \ddots\end{bmatrix}V^\top$$
and $A^\top A$ is semi-positive definite!  
Therefore, we can find $A^\top A = Q\Lambda Q^\top$ and we can find $V$ and $\Sigma$.  

Using the same method, we can find $AA^\top =  U\Sigma V^\top V\Sigma^\top U^\top = U\Sigma U^\top$ and again $AA^\top$ is semi-positive definite, so we can do another $AA^\top = Q'\Lambda' Q'^\top$ to find $U$ and $\Sigma$.  
However using this method, $U$ might not be consistent with $V$, and the following construction is much better:  
Since we hope $U$ satisfies $AV = U\Sigma$,
let $u_i = \dfrac{Av_i}{\sigma_i}$.  
We want to show that $u_i$ is orthonormal. By evaluating, 
$$u_i^\top u_i = \dfrac{v_i^\top A^\top}{\sigma_i}\dfrac{Av_i}{\sigma_i} = \dfrac{v_i^\top \sigma_i^2 v_i}{\sigma_i^2} = 1$$
$$u_i^\top u_j = \dfrac{v_i^\top A^\top}{\sigma_i}\dfrac{Av_j}{\sigma_j} = \dfrac{v_i^\top \sigma_j^2 v_j}{\sigma_i\sigma_j} = 0$$
Therefore if $m \leq n$, we can directly make 
$$U = \begin{bmatrix}u_1 & u_2 & \cdots & u_m \end{bmatrix}, \Sigma = \begin{bmatrix}\sigma_1 \\ & \sigma_2 \\ && \ddots \\ &&& \sigma_m & 0 & \cdots \end{bmatrix}$$
Otherwise we can fill up $U$ using Gram-Schmidt process (by taking the null spaces) as

$$U = \begin{bmatrix}u_1 & u_2 & \cdots & u_m \end{bmatrix}, \Sigma = \begin{bmatrix}\sigma_1 \\ & \sigma_2 \\ && \ddots \\ &&& \sigma_n \\ &&& 0 \\ &&& \vdots \end{bmatrix}$$

An interesting fact is that if $\mathrm{rank}(A) = r$,  
$v_{[1, r]}$ are the orthonormal basis of row space,  
$u_{[1, r]}$ are the orthonormal basis of column space,  
$v_{[r + 1, n]}$ are the orthonormal basis of null space,  
$u_{[r + 1, m]}$ are the orthonormal basis of left null space.  

\[Lecture 30 starts here]
 
