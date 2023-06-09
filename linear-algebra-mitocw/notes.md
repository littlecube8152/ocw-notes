 
Texts wrapped in
> this style are the notes not included in the tape. 

\[Lecture 01 starts here\]
## Linear algebra is a study about **linear equations**.
## Linear equations - three perspectives

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

Well, before we go to the solution of the original equation, let's see will the elimination work in every case?
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
## Matrix Multiplication - Five Approaches
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
$(A^{-1}A)^T = I^T$  
$A^T(A^{-1})^T = I$  
Therefore it is $(A^{-1})^T$.  

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
A cool fact is that, the inverse of $P$, $P^{-1}$, is actually identical to the transpose of $P$, $P^T$.

## Transpose
Basic rule:
$$(AB)^T = B^TA^T$$
Symmetric matrices are the matrices satisfying
$$A = A^T$$
And we have the following property:
**Property.** For any matrix $A$, $AA^T$ is symmetric.
*Proof.* 
$$(AA^T)^T = A^{TT}A^T = AA^T$$
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
We already solved all solutions of $Ax = \mathbf 0$, then what about the general problem: solving $Ax = b$?
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
 3. Row space $C(A^T)  \subset \mathbb R^n$
 4. Left null space $N(A^T)  \subset \mathbb R^m$

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
$$A^Ty = \mathbf 0$$
Transpose both side yields
$$y^TA = \mathbf 0^T$$
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
$$\dim C(A^T) + \dim N(A^T) = m$$
$$\dim C(A) = \dim C(A^T)$$
The first two are pretty obvious according to the definition, and the last can be observed that the pivot columns have the same number of non-zero rows, thus they have the same dimension.  

\[Lecture 11 starts here]

## Other Spaces
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

## Rank 1 matrices

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
  $$ A^Ty=\mathbf 0$$
  $$\begin{bmatrix}-1 & 0 & -1 & -1 & 0 \\ 1 & -1 & 0 & 0 & 0 \\ 0 & 1 & 1 & 0 & -1 \\ 0 & 0 & 0 & 1 & 1 \end{bmatrix}\begin{bmatrix}y_1 \\ y_2 \\ y_3 \\ y_4 \\ y_5\end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \\ 0\end{bmatrix}$$
  Solving the left null space, $N(A^T)$, tells us what are the stable states. In fact, the basis of the null space are *circuits*.  
  Assume the graph is *connected*, we have the following identity:
  $$\text{\#nodes } - \text{\#edges +} \dim N(A^T) = 1$$ 
  In physics, this is called **Kirchhoff's Current Law**.  

Using Ohm's Law, the two aspects of incidence matrix can be united into a single equation.  

\[Lecture 13 is about Quiz 1]  
\[Lecture 14 starts here]

## Orthogonal

Two column matrices $x, y$ are called **orthogonal** ($x \perp y$) if
$$x^Ty = \mathbf 0$$

**Property.** Let $\|x\|^2 = x^Tx$. $x$ and $y$ are orthogonal if and only if
$$\|x\|^2 + \|y\|^2 = \|x+y\|^2$$
*Proof.* Expand RHS gives 
$$x^Tx + x^Ty + y^Tx + y^Ty = x^Tx + y^Ty = \|x\|^2 + \|y\|^2$$

**Definition.** Subspace $S$ is called **orthogonal to** subspace $T$ if 
$$\forall s \in S, \forall t \in T, s^Tt = \mathbf 0$$

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
$$u^Tx = (c_1 u_1 + c_2 u_2 + \cdots + c_m u_m)^Tx = 0 + 0 + \cdots + 0 = 0$$
For the same reason, column space is orthogonal to the left null space.  

Not only they are orthogonal, they are *orthogonal complements* in $\mathbb R^n$, which means null space contains *all* vectors that are orthogonal to the (all the elements in) the row space and vice versa.  

\[Lecture 15 starts here]
