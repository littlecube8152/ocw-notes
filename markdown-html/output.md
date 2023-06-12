 
Texts wrapped in
> this style are the notes not included in the tape. 

Some order of contents might not match with the tape because I would like to put relevant contents together, place motivation before introducing something (why would you learn something for nothing?)



---
Linear algebra is a study about **linear equations**.
---

\[Lecture 01 starts here\]

## Linear equations

There are three perspective of a system of linear equations, say {{cc09daba676fcefcfb20c1e9e42db1b746b5953e04532813493b40fb4841c60e}} equations and {{bb28a9b83048a0f36a72a56394914040f7f0171b49534f6138053bdd68916943}} variables,
1. **Row picture**. It is how we see the equations. In two dimensions, it looks like lines intersecting each others, and in three dimensions, it looks like plane intersecting each others.
2. **Column picture**. It is to treat the equations as linear combinations of vectors.
3. **Matrix picture**. It is to combine the two aforementioned picture into a matrix form. 

For equation {{0d39f0493790b86abb68ba8319c2c7c096576a5753f1829bc5d0d8736970e79f}}, we think it as "can {{00511bf0a6978c2c0834726bdea81630ee1b0d33f80bc837d9bda37ad4212cd6}} be represented by linear combination of columns of {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}}?"

Some examples.

|Row picture |Column picture |Matrix picture|
|:-|:-|:-|
|{{910a95eeefa0c29e704b509af9952092911f91d6a0010f28a7f4f74f6ec1735f}}|{{6081264846fbfee8b2f0e8630c1c0edadc5bd033c17d39f81fc5cfb9a4428310}}|{{a4e4abd67b1afd0085f6f3abc90d057e8afbf596a86f93fa31a7d2c81d1bbaba}}|
|{{efd55fae4b168711abc6e1f51023e5a3af1c4a1a1dd040bb26d18e92048a17d5}}|{{06b8c30ed9af8acb8455fd5da336c189f679c47c687b66372e1f9119b4463e0d}}|{{0dd2f82e2c359f99ac38536df015a9171bc456926fe30dcad1f354c171b23f45}}|

Can I solve every {{0d39f0493790b86abb68ba8319c2c7c096576a5753f1829bc5d0d8736970e79f}} for every {{00511bf0a6978c2c0834726bdea81630ee1b0d33f80bc837d9bda37ad4212cd6}}?
Which is, do all the linear combinations of all columns of {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} fills the whole dimension?

\[Lecture 02 starts here]
## Eliminations
How do we solve a system of equations algorithmic? Eliminations.
Our idea is to make the matrix {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} triangular, so we can back-substitute the variables with ease.

Example.
Suppose the equation we would like to solve is 

{{bc2f1ae2d71660b833a167974d171fc90e39d89a70a0a3be334493e7a3f0ecb0}}

Then the matrix {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} will be

{{ec90db74e98d525b16949821bd9a4572342178e05366300fa1660efea70d9529}}

First, we aim to eliminate the first column, so we select row 1 column 1 as the pivot.

{{9a7171e02f408604ba752a21d589d60b4898c1eec4b73f39626ed9f42f210948}}

Then we subtract three times row 1 from row 2, making row 2 column 1 zero.

{{067cb678e7171621a39f49610ed3223d07e03926029c7b8b55d02be6be595b28}}

Row 3 column 1 is already zero so we do nothing here.

{{fb42b6cf98f6fc712413feb154e73a6c91f5f4150a424b124f5f1cfc2ee3dbba}}

Now we are left with two variables (column 2, 3) and two equations, (row 2, 3). We do what we have done recursively.
Select row 1 column 1 as the pivot.

{{a580ac97a89796431ad2cb460f7e68dc350b7528db91aca8b7523feeebd40e49}}

Then we subtract two times row 2 from row 3 to eliminate the four.

{{71a0fbc34db931fa0063abe72564b55bde8e13fea69dccb890e97961cc0e6e99}}

Then only one row and one column are left, and we are done!

Well, before we go to the solution of the original equation, let's see will the elimination work in every case?
Obvious no, if at some point we are not able to choose a pivot, that is, the column we are dealing with are left with all zeros.

Let's head back to the solution. We put the constant term in column 4 and solve it, this called **augmented matrix**.

{{ce29baf9c8d0e76a2bade17fab50c3b85d45b1eb258f63e4ab533ef01f267434}}

Now we know that

{{4ab2d0a94afebe058fedfebc6f97a67ea19ae2aecf4bc893ee6e90061fe7196b}}

Which has a (also the only) solution

{{1d911b7ec2f4378d2409aa1522121c1964850b1dd04f79303a3a1a50b394dd73}}


### Elimination Matrix
In the column picture, we take multiplying a matrix by a column matrix as **taking the linear combination of each column**.
Say we multiply
{{5f8f18ae44dc30228c1185d54ae7b9554bb67d06eccaaf2ea23f6a8f7af4441f}}
and we get a column matrix.

Now we are dealing with mostly row operations, and if we multiplying a row matrix by a matrix, we are **taking the linear combination of each row**.
{{9ef6baa7ba83b3776c262740dcbe7f07fb43f78f75b9234e397acd48837280ad}}

**This is how we want the matrix multiplication to be. If we want column picture, we multiply on the right. If we want row picture, we multiply on the left. Matrix is a way to unite two different perspectives.** 

Head back to our elimination, how can we speak it in the language of matrix?
{{1ebd1bed878a93ff0be104ae61f1e4162e5178bf998cd163a96304fd38e72ab3}}
We want that {{bf79cc576d5eade315f71af97bdbd98ea5e804e2fc94d23be5c2ba3542c39069}} subtracts three times row 1 from row 2 and do nothing about other rows. We are doing row operations so we put it on the left side.
Recall that row matrices are "linear combinations of rows", so 
{{2485ae8e6599973a33b9a4d1566253366532d5e2ba1108bd1fcb034a057c30c1}}
Also for the second step, we want to find some {{590d96f9f23977868bda148ffaa70bc7427d24d1fdc985be0bde1413a69254ea}} satisfying 
{{6081bea1e24f5567e19c25b9717e2e4de52ad5c1bb473411e2c7f47e2e59e88f}}
and it is
{{cbb13ddea3b1ad2d76938ee100d35f46195a9bc04163a1f9705eef0f9da1d63e}}

Let we denote the final result as {{77e20b8c0fd244389059c1bf04a3a6e065820ec77fa9ca323d829d6c5b908381}}, then we know that
{{4d80fced574e5f0eef7617d01a2f3debbe6d92b131e92b76d8f251fb32e16337}}
In fact, we can change the parentheses, which means
{{bd67e95d98a07960ffe6d2cc9dbfc0832f1f965c7c7bb9625cd843a9844bc393}}
is also correct, and we have a matrix {{da324fbf535b7f0b765ebfce09107559d38e564458960c017fd4d16c263114eb}} that does all the work.

\[Lecture 03 starts here]
## Matrix Multiplication
Say we multiply two matrices {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} and {{ccd2b4a0ba379d8f9711b5dbc84d5b71c498d82e403f940904c5bf9cfb31d181}}, and the result would be {{2a6f81ee63754c7772494d0f9901d5bdfb837dc7cd3bc5eff66467bd08dee26f}}.
Now we use the respective lowercase of the matrix name to represent its corresponding elements, for example, {{b1239cf3d4be0cadfb37e3ac2bce67221c4004e1f5ae4d4a4a42eb9846205bfe}} means the element in {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} at row 1 column 2.
1. **Multiply rows by columns - the definition**
	Two matrices can be multiplied together if their the number of the rows in the first one is the same with the number of the columns in the second one (which is kind of obvious if you look at the row picture or the column picture). 
	Let's say that {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} is a {{cc09daba676fcefcfb20c1e9e42db1b746b5953e04532813493b40fb4841c60e}} by {{bb28a9b83048a0f36a72a56394914040f7f0171b49534f6138053bdd68916943}} matrix (which means there are {{cc09daba676fcefcfb20c1e9e42db1b746b5953e04532813493b40fb4841c60e}} rows and {{bb28a9b83048a0f36a72a56394914040f7f0171b49534f6138053bdd68916943}} columns in {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}}) and {{ccd2b4a0ba379d8f9711b5dbc84d5b71c498d82e403f940904c5bf9cfb31d181}} is a {{bb28a9b83048a0f36a72a56394914040f7f0171b49534f6138053bdd68916943}} by {{ea6649a9e145c333693e04f2dfe6435ea3f67511edf186c7d4e9dc63058f446e}} matrix.
	Then the result of multiplication {{a6c326f32c4c106d6a9ad6f25b278dfca623f0f93bcaace85fd2871ee846c377}}, is a {{980e7b131d61cb7b0c6b7d6c16d98ac2b8644515610066848e451a7a5556aad2}} matrix where each elements is defined as below:
{{0f0037860daf697f1ba4978ff072504729252671c4ea989f0027db75a1620ded}}
 Which is, for {{e7b2e8454df63375b0397925c066f5373f2e2468c29e099eaae8b7dd282ac076}}, we take the {{566ce35497d2b07c5147093d9ed70d8e54fdfbb259f9ad5d2607533994a1a6d8}}-th row of {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} and the {{27c5fdea0894415e9af99f00ea9e5e6438cea043c4715982465fd9d85b6185f6}}-th row of {{ccd2b4a0ba379d8f9711b5dbc84d5b71c498d82e403f940904c5bf9cfb31d181}} and take their dot products.  
	{{d297812c211a2c0a2d59898660749f2bd720ce158e9e4bebfb9aecd4937b7d93}}
2. **Multiply columns by columns**
	Well, we can also take the column picture, where each column of {{ccd2b4a0ba379d8f9711b5dbc84d5b71c498d82e403f940904c5bf9cfb31d181}} produces a column which is the linear combination of the columns in {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}}, and we concatenate them in order.  
	{{b7b16f9bf87b60ece40b4651581c86093bd1c690c5684e8441b78783de9b82ec}}
3. **Multiply rows by rows**
	Row picture also works this way, and it is clear so there is going to be only illustrations.  
	{{a50d144b62b40fb56fc9b0220abb39457723d99f0e9792fbbe4621d1b992ca0f}}
4. **Multiply columns by rows**
	What if we do the only left possibility, multiply columns by rows?  
	In this way, we take the {{2725b2d0fc640cb2728a1834f8c41d47e601a7313494a3c35628268f485f3a5f}}-th row of {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} and the {{2725b2d0fc640cb2728a1834f8c41d47e601a7313494a3c35628268f485f3a5f}}-th row of {{ccd2b4a0ba379d8f9711b5dbc84d5b71c498d82e403f940904c5bf9cfb31d181}} and they multiply into a {{15ffcb07793c1bb960dd61765d3150dbe22ee246f09c69882bef5fe6468c929b}} matrix.  
	And we have {{bb28a9b83048a0f36a72a56394914040f7f0171b49534f6138053bdd68916943}} of them, adding them up we get {{2a6f81ee63754c7772494d0f9901d5bdfb837dc7cd3bc5eff66467bd08dee26f}} in the end.  
	In computers, this is the best way we have since it has the best cache.  
5. Block Multiplication
	Instead of doing the full matrix multiplication at once, we can chop them into chunks, say we have
	{{c3fa9a9ce593d95e93bd3ef34df9d7769d1a964a6e27e8f51765d8d64d40b82b}}  
	As long as the size is consistent with each others, we can do multiplication in this way:
	{{4494b82a3ee6a46e008d9eedc8c115e7555c7a1fa2650aaadd14465ca43cb79e}}  
	which is kind of, resembling the {{f1143f1add165a2ebac51a6145723f8dc55a287fac9f0d9947a2ca57ab705c90}} multiplication.

## Inverse (of square matrices)
For every square matrix {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}}, is there another matrix {{5211c79c996313d4b08b339133ea94b2f273db96aeecc2ae22c4625f789ada88}} satisfying {{a4fcb7eb4064f13efd6ba47222302cc5b5e2a83c10b48f7562a28f1fbc001721}}?  
If {{5211c79c996313d4b08b339133ea94b2f273db96aeecc2ae22c4625f789ada88}} does exist, then {{0004a0b818a6dab259497a5b6b7df74652ed3f78c55159efcb8beaadfcd30374}}.

For those which have an inverse, they are called **invertible matrices** or **non-singular matrices**.
For those which do not have an inverse, they are called **singular matrices**.

**Property.** A matrix {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} is singular matrix if there is a non-zero {{16731395c9a7bcef39d0e38e101c58677488a539c84314a2b1276242dcb1b8c7}} satisfies {{46ed22e41d40253ca1a92e5fac526568f2ee90050c3fdabf5d8f112fa37291f5}}.  
> Assume that {{5211c79c996313d4b08b339133ea94b2f273db96aeecc2ae22c4625f789ada88}} exists, then we have {{95c266c6d31589bf8aefa868dade4081de3d662e6a45f73f8d05a1c3fd95e27a}}, which means {{6a9bf3ee9e2b361aa93f661054742a6399682dcbae870c621bb64ed482462502}} and we get a contradiction.

> Thus we know for each column matrix of size {{bb28a9b83048a0f36a72a56394914040f7f0171b49534f6138053bdd68916943}}, {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} is a way to map each column matrix to another matrix, such that no two matrices have the same output.
> Assume that {{5211c79c996313d4b08b339133ea94b2f273db96aeecc2ae22c4625f789ada88}} exists, then {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} and {{5211c79c996313d4b08b339133ea94b2f273db96aeecc2ae22c4625f789ada88}} can be treated as two functions which are the inverse of each other, thus {{957082d1c6f4fe6f7a2f670a8801eb7f4f7d8f58629f3d04e08282a8d15842fd}}.  
> Also we can imply that the property is actually the sufficient and necessary condition of singular matrices.  

Let's take a look of {{f1143f1add165a2ebac51a6145723f8dc55a287fac9f0d9947a2ca57ab705c90}} matrices, when does {{a3460c82c91e5b81665e9274977fb5cf8eb3dd4aac41767fa495eef1b53ae6c6}} have an inverse?  
{{6400664cc80a95b86f767b963c99859cb598418bf678560df0d8e410139331be}}, which means there is a solution for the two system:  
{{4a0754cbb9b76600907a7cac09888ca3e175d12b3b3d15f123046f5309997859}}  
{{a0d043658a8381121404aa8bf31d31b826ab4a088713481aa55c2ea63f77e46f}}  
When we expand it, they have the same coefficient for the {{22bf003d6cac79e1d917cacdab9539c5d59468c02c22d29c08df00834ee4bbe6}} and the {{bead6513981f86c92c1b955f22650cf775ed108fa2975e5e5866501cd938a193}} terms, but not the constant ones.
Then we are going to introduce Gauss-Jordan Elimination, which is capable of solving multiple system with the same coefficient of variables at the same time.

### Gauss-Jordan Elimination
In order to find the inverse, we put {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} on the left side and {{4a1f941b3c6f426ec08de78c17e2f80f07a8b789701ba6b25126da00fab1231c}} on the right side, combined into a single long matrix (an **augmented matrix**).  

{{d2eca6c5e42d75e7f26e5a89d20f58fa60cc2708db578b262f9f3d55f81c8b24}}
  
And we keep doing row operations, until the left side becomes {{4a1f941b3c6f426ec08de78c17e2f80f07a8b789701ba6b25126da00fab1231c}} and the right side is {{5211c79c996313d4b08b339133ea94b2f273db96aeecc2ae22c4625f789ada88}}. Why is that?  
Recall row operations are matrices, let's say we have done {{191ff720bbe971ffcd0988d17a5bcb3d451f730d681d58c772fbae3287e0774f}} in order. Since we are in row pictures, we can break the augmented matrix into two matrices, and because of the associative law, we denote {{31757aae189f045a9c0f14808e2ab4d71c60816983154e31636799f537ff437d}} as {{6ea72f457f8aca38b17dc9410a1775ab08ce177a6df93e9281d0bedae07b5861}}.  
Then we have {{4ea2da02ba9f038428ce1666f772a1092891bf1cbaf265489dedab07d45af28f}}, which means {{e6caed0602bd828d7155d2a4d39dc8cd016a94ea927c22304637e82cc03e4390}} and on the right side we have {{21bd4275cede96b72d826ff7ca87b5a755dd21bf39ace9e3c3ff9ce660439b14}}, which is why it works magically for every invertible matrix.

\[Lecture 04 starts here]
### More inverses
Inverse of {{f8f91963e7fb42c59e96faed100ae027f63f29abd9c636909303007e7dd5a30b}}? {{526a6b69892e7deaa379049cd7b093205f3c0161fdd95d520ca7ba5ea6354307}}. (Check it for both sides!)  
Inverse of {{2a158231be86b84770fb8e0238031360dc9c2701cb7353af28444a7efd3d6eff}}?  
{{44e2574532dfc0e3892aafa5f26178149903ee15d01b167cc08037de76eddd15}}  
{{28a9225c505e86d8f2572f24511a9e4c9817dcea75cd674613163fe839d1bd6c}}  
Therefore it is {{c202f06b95f109b5d15a494861054fdd92031e68c53ac310cb55a52f615a583a}}.  

## LU-factorization (decomposition)
> Purposes of {{f100e37d91f6e265d274e59215e069feadc6b6335d7fe64185cf270e21468804}}-factorization:
> 1. It is another way to interpret Gauss Elimination.
> 2. In computation, for a fixed {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}}, a {{2e7e0fda85cbac2daa211d325a1df218b01b97af174187de478d433432ed2321}} matrix, solving {{7a972db4806577ebad9da3316b822dc27b3282cc39e03983f6237922c19941e2}} is {{378b81eed5af0cfca367a4edb2d84a67715e143565bd05fc11d24f3cb2062d3a}} each time. However for upper-triangle matrices and lower-triangle matrices, solving {{a50f3d1ef0bdba9ce8351cbd9e93d3725298971abdbee4ec22de89a3a85adbbd}} or {{ca10c9ebec5c15f8f6fc235c8be8fa4c10fa061f74b4b131a6afacb9cfff59a1}} is {{10027a56e1fdfc0a40f14ddb729a8fdc52499ec6a8a4f9c2d6711c8e446e9de7}} (because the elimination is easier each steps, almost identical to back substitution). Since in many applications of linear algebra, {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} is fixed during the whole procedure, {{f100e37d91f6e265d274e59215e069feadc6b6335d7fe64185cf270e21468804}} decomposition comes in handy since it reduces time significantly.  
> 	Notice that even we have the inverse matrix, matrix multiplication still takes {{04055fc0c5fe3d5ed9651a24dbfe37653b30c6b574118ef151e3bab3ecd39ea5}} time and {{f100e37d91f6e265d274e59215e069feadc6b6335d7fe64185cf270e21468804}}-factorization is still far better (at least at the moment I am writing this note).

Recall what we have learnt about elimination, our goal is

{{94c1c2d793dcdb171cb527b67e6a1ecd719e7978043ed5af75f77f3d27e6e7c7}}

How do we find {{41ff4a272b32b4a11adfab661d1b963604839c50b6f502ad55c84fdc5b1177ce}}? We already have the elimination matrices:

{{19a1634e001ecc279099fc76491345370f7e104dd3907a5a527c2168590e7273}}

For these elimination matrices, they are easy to "undo" them. Every row operation we have done is subtract {{2725b2d0fc640cb2728a1834f8c41d47e601a7313494a3c35628268f485f3a5f}} times row {{566ce35497d2b07c5147093d9ed70d8e54fdfbb259f9ad5d2607533994a1a6d8}} from row {{27c5fdea0894415e9af99f00ea9e5e6438cea043c4715982465fd9d85b6185f6}}. To undo it, we just add back {{2725b2d0fc640cb2728a1834f8c41d47e601a7313494a3c35628268f485f3a5f}} times row {{566ce35497d2b07c5147093d9ed70d8e54fdfbb259f9ad5d2607533994a1a6d8}} to row {{27c5fdea0894415e9af99f00ea9e5e6438cea043c4715982465fd9d85b6185f6}}, and it is easy to verify this is the inverse matrix.
Therefore we can do this:

{{197323be6492753a4a7fbb2339bf1aa333cb11c477eb97ee703bba5aced3575c}}

And we have 

{{f3eb873bf948236e21ceee7b6226c61f0a7f7757b6c0cbddc7afb573c639730e}}

which means 

{{d55340386323e154fd78205873fa7f0fe120e19d8b745462068051d0bf712d39}}

For now, we ignore the troublesome matrices, which gives zero when performing elimination. 
The cool thing is, multiplying any two lower-triangular matrices obtains another lower-triangular matrix, so {{41ff4a272b32b4a11adfab661d1b963604839c50b6f502ad55c84fdc5b1177ce}} must be a lower-triangular matrix.  
And if we want there are all {{72bc3c1b3553a71d525d8715f4963adfb2b8e7e18c32f0b1b651f3e841526770}}s in the main diagonal, we can always do

{{a4719c1a48cf04ab7f7d1fda71410e1c97f1f946b4aa21acb082e7bacf1330c3}}

where {{3a16fddd1da7699eacf47cfa3f73a53f8176dd10cda11e68d6a4b5424b1c8285}} is a diagonal matrix (which means any elements not lying on the main diagonal is zero).

\[Lecture 05 start here]
### Permuting allowed
Sometimes {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} is good enough to perform elimination without failing to pick a pivot, but for all invertible matrices, it is not always the case.
Therefore we are introducing the idea of permutation matrices. With permuting allowed, every invertible matrix is able to do the LU-factorization.

{{f4a7a6c4f5990a41980c7761dd2ab587c23148797c192f9a685ebb3133541bad}}

A permutation matrix {{83e05657563b28cf0b63748e1c794cad196c106a2c5499d9fa561d9a35e7f865}} is a square matrix which has exactly one {{72bc3c1b3553a71d525d8715f4963adfb2b8e7e18c32f0b1b651f3e841526770}} in each row and column, and other elements are all {{04059783893b129d925417c55e95e559c8d4be599ebd2ca55aa2472bc9007f90}}.
In the previous section, {{3df069fa7652a9c915026681b94a68244ab6af22a2b846c3130fdc519dd483fc}}, which means no row exchanges are performed.
From the row picture, we can see what {{83e05657563b28cf0b63748e1c794cad196c106a2c5499d9fa561d9a35e7f865}} does is exactly permuting the rows.
A cool fact is that, the inverse of {{83e05657563b28cf0b63748e1c794cad196c106a2c5499d9fa561d9a35e7f865}}, {{8183eae3a872b3a428cedcce29251a8da123efea433ba9b3528bf0705d9c7c66}}, is actually identical to the transpose of {{83e05657563b28cf0b63748e1c794cad196c106a2c5499d9fa561d9a35e7f865}}, {{fb7a50a6b5faf02a8f298d301afa55a9603aae48d418fc478389cc6a85df75a7}}.

## Transpose
Basic rule:

{{39de4cf9db4efa1a1ce28dd5dbac31c248f9417dd4e874486e04fb7596d9165b}}

Symmetric matrices are the matrices satisfying

{{f3129e9d715e8b9c0b8dade26acc6780129a26e5fd4e0c03bcf92ca4ca823a54}}

And we have the following property:
**Property.** For any matrix {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}}, {{0533361c09337ae0e1b6248facccbfe114d9fe65d710d21295fa24a3bcb6ea60}} is symmetric.
*Proof.* 

{{f09f11288e3816c9a44a3789a3776021eb6b334eab24e1603d599083ed5080b5}}

\[Lecture 06 starts here]
## Vector Spaces - A Generalization of Vectors
A vector space is a set of vectors which supports scalar multiplication and addition (which is what we have used to solve linear equations so far).
To generalize the idea, a vector space is a set of vectors {{da8c27c394be59d9d79201471429ba3328591059253284e430ee5c6965e2f2f9}} over a field {{ece49feba00b8a1812ded074f725361efa66b3c98a069a56aeb4b360bb7aee93}}.
It has to support the following axioms.

The first two are operations, and the remain eight are vector space axioms. 
If not mentioned, we assume it should be hold for any {{86f059479278e82bbf93881c668258191f384234e94dba2487b8a12178bad549}} and {{95ae2f3baea45b88dcfb30912afdc5f4eb87a2ee5d0235c9b82fac60090fb804}}.

|Meaning |Definition |
|-|-|
|Addition |{{5189eb0cfbc5260f63b3b2f8ee8fff5f349ae9784e8d866048c1b50ee55c0d37}}|
|Scalar Multiplication |{{00b7fa33d731066cb5c290548a43ca2b7d1e94b4012b6530c962349ad336635b}}|
|Associativity|{{c71fbda4b14613bbe11c061c5a0eebf8173c7e8ad0ffa4c79a2b6be24291db1e}}|
|Commutativity|{{20ace3bebba83ec156e7e631333bbbaffe5e54f8ad6c1c79bdb1fe4af0d950a5}}|
|Identity element (of addition)|{{9b308582b757f3462cb78a999330eca99e322ffa396bb589d13490b293042911}} s.t. {{941baac9e98143dcedc7fcb560d6cac65bcc735fb022c5ee1488ba282383cf4b}}|
|Identity element (of multiplication)|{{bd8728e3e495cf83eff0deecd7bd345340e84bd0143843c81f8fa1c7a0b436e7}} s.t. {{4aeb32944de37267e4e10e01a9f6401f5e53de4da4259ad867c49f40a30e8004}}|
|Inverse elements|{{a8f38613e6ccae183eff62fbaab31673cce3aa93d307a85d0db712fe2960e4d4}} s.t. {{1f3b68ba955b9a057c1733e53677ffa5d3e0b96434c4b47ddec278405df3876e}}
|Compatibility (of scalars)\*|{{b4bf326ba35dbb8bbd6170f73a5125005b1836a10e9eccfd53c6033593fc868f}}
|Distributivity (of vectors)|{{e4b517ebc61b2c02b288e46c958606d70746da77feb0c2d136f4a8d8c9b546a0}}
|Distributivity (of scalars)|{{6b885d77c1a536481e76ffb960212531e1c1b928de5ff47493c9eaf4e92cbe10}}
\* Note: associativity of scalars are defined by fields, and vector spaces are good with the non-associative fields.

There are many examples. In fact, for any positive integer {{bb28a9b83048a0f36a72a56394914040f7f0171b49534f6138053bdd68916943}}, {{0d34742bc8eaac8129622066a94d8759199ce89b472a10ddcbfde47aa8e40fe9}} is a vector space over {{836bc477316b3cac40386d3b4fede9344123e13cb2876d2103fc2b7124ee51e2}} (and it is easy to verify that).

### Subspaces
**Definition.** A set {{be46397f74b9bd19d55eeb6fb897a8ade867fd33055655ddba94546e993eab20}}, where {{da8c27c394be59d9d79201471429ba3328591059253284e430ee5c6965e2f2f9}} is a vector space over {{ece49feba00b8a1812ded074f725361efa66b3c98a069a56aeb4b360bb7aee93}}, is called a subspaces if {{fdf30f5db1f3424874da244595a2db648c7b056dc537a2b62eb64b4d26d827ef}} is a vector space over {{ece49feba00b8a1812ded074f725361efa66b3c98a069a56aeb4b360bb7aee93}} with the same addition and scalar multiplication operations.

**Property.** For two subspaces of {{da8c27c394be59d9d79201471429ba3328591059253284e430ee5c6965e2f2f9}}, say {{fdf30f5db1f3424874da244595a2db648c7b056dc537a2b62eb64b4d26d827ef}} and {{cd15d3a571b67c26cfa4d135c0beb323c631d85844625699d123761440301d5d}}, their intersection forms another subspace, but their union is not always another subspace.

Notice that when regarding subspaces, many of the axioms are actually applied to the operations directly, so we can only check if the addition and scalar multiplication is closed in the set and zero is present.

### Column Spaces
Assume we are in {{0d34742bc8eaac8129622066a94d8759199ce89b472a10ddcbfde47aa8e40fe9}}, a {{0f6ddc3e7995d3cddd311d016e3814d9bc89de0c544d17babec62a0aab792c0c}} matrix {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} forms a column space, which is a subspace of {{0d34742bc8eaac8129622066a94d8759199ce89b472a10ddcbfde47aa8e40fe9}}, defined as follows:

{{566ec39a33fba724f3cc21fa6f682a03bca992b7bd7233f7f70f5d9de034becb}}

In other words, we put all linear combinations of columns of {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} in the set.
Now we start to think of, does {{56d1910ade815ed546930d65d2ba35dcb0f4d29fb2cc8375c230ab262b0a2261}} fill the whole {{0d34742bc8eaac8129622066a94d8759199ce89b472a10ddcbfde47aa8e40fe9}}? If not always, how much is {{56d1910ade815ed546930d65d2ba35dcb0f4d29fb2cc8375c230ab262b0a2261}} filling?
The answer is,

{{0ece4e3e342a48e0f22872175b21867b488556aefa8f70f6004604368adc5fd4}}

which is equivalent to the definition above.

### Null Spaces
Assume we are in {{7dfe407aa753952af7be84c0da11c819e53633250912a51f0077b24500305131}}, a {{0f6ddc3e7995d3cddd311d016e3814d9bc89de0c544d17babec62a0aab792c0c}} matrix {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} not only forms a column space but also forms a **null space**, which is a subspace of {{7dfe407aa753952af7be84c0da11c819e53633250912a51f0077b24500305131}}, defined as follows:

{{a95fd8d5d8212ef812bf369ddffc4561dea159985ab1d4b77634165e5c49fc01}}

{{3c41ab82404b92ba66789b91a0708dfe8056842a6f99375e37641526f2eb3796}} is definitely in the set. For any scalars, {{5f183cb583fe981a98efcc3993c5e7e5f0846a3346a87fb55d7103634f04ea13}} is still in the set, and for any vectors, their combination, say {{5a4691af590dc6f98c93782396204d513909c5be422983756cdc3d82261397ef}}, still equals to {{3c41ab82404b92ba66789b91a0708dfe8056842a6f99375e37641526f2eb3796}}.

\[Lecture 07 starts here]
> Why is null spaces important?  
> As mentioned before, with {{378b81eed5af0cfca367a4edb2d84a67715e143565bd05fc11d24f3cb2062d3a}} pre-processing, we can obtain any solution of {{7a972db4806577ebad9da3316b822dc27b3282cc39e03983f6237922c19941e2}} under {{10027a56e1fdfc0a40f14ddb729a8fdc52499ec6a8a4f9c2d6711c8e446e9de7}}. Well, that applies only if {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} is invertible.  
> With null spaces, we can know if {{7a972db4806577ebad9da3316b822dc27b3282cc39e03983f6237922c19941e2}} has a unique solution, and if not, we can even know all the solutions under {{10027a56e1fdfc0a40f14ddb729a8fdc52499ec6a8a4f9c2d6711c8e446e9de7}}. Back-substitution takes {{378b81eed5af0cfca367a4edb2d84a67715e143565bd05fc11d24f3cb2062d3a}} if there are more than one solution (since in {{566ce35497d2b07c5147093d9ed70d8e54fdfbb259f9ad5d2607533994a1a6d8}}-th step there are at most {{566ce35497d2b07c5147093d9ed70d8e54fdfbb259f9ad5d2607533994a1a6d8}} free variables, and back-substitution would take {{7ac8636f153cfc23abf3fb8d5762575a173bd5197bb6b362f062b6483f2313f0}} times. Summing them up gets {{378b81eed5af0cfca367a4edb2d84a67715e143565bd05fc11d24f3cb2062d3a}}.)

#### Row Echelon Form

Now we try to find null spaces of a matrix, and we need a working algorithm.
Let's start with an example, say

{{4e7c70b13acabbc7cd993cb3b48749e739ca26e7e6431141bca0255dbc25cba1}}

Now we try to apply elimination, since for any elimination matrix or permutation matrix {{31757aae189f045a9c0f14808e2ab4d71c60816983154e31636799f537ff437d}},

{{2922e072e5efef558f734c9269f337a9e6e14d3df5bcb321f6e519e76c623959}}

the algorithm still works, so let's see.

{{41c4b5ecd09ec024c5a08c58bf6790cc31bd55e5b285183e3a5564769ab5e6e6}}

We call the result {{77e20b8c0fd244389059c1bf04a3a6e065820ec77fa9ca323d829d6c5b908381}}, a matrix with a staircase-looking zeroes, is the **(row) echelon form**.
This matrix represents

{{33ff4b718baba03cc9424e8bb71b3b5b793fee0f30ccb468d3cf28faaa23243c}}

which only have 2 equations but 4 unknowns, and it seems there is still a lot of space left for the solutions.  
Therefore we introduce how do we describe "how free the solutions are".  
The **rank** of {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} is defined as the number of pivots during the elimination.
And we say the columns which contains pivots are **pivot columns** and the rest of them are **free columns**.  
Why is it called **free columns**? Because they does not contain important pivots, and we could cancel out them by adjusting pivot columns.  
What it takes to eliminate 1 column 2? We take negative 2 times of column 1, therefore one of the solutions is

{{5a8a57d242865c63a299618f3701385561886428971c2bf033488d1d6bd8f318}}

What it takes to eliminate 1 column 4? We take negative 2 times of column 3 and 2 times of column 1, therefore another solution is

{{d6d4055c96286502f2a5dcc3ff6005399eef889e3302c40adc40079d4fa40003}}

And we could take all of the linear combinations, thus the null space of {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} is

{{12313abe98e2f0cb60c9959243931dfc9ffd7a0800ef6bb65fbd7ce598d7cbad}}

What does "rank" mean? It means there are {{8425221e3c04b4782294a7fa0b6292579721720e87a05b4748a0faaf56d11782}} number of free columns, which means the solutions are the linear combinations of these {{8425221e3c04b4782294a7fa0b6292579721720e87a05b4748a0faaf56d11782}} vectors. In this case, we have {{b71be43b02045b8b4173d0bc2a348d09d5082ab0b79985e03def8bb55c796534}} of them.

#### Reduced Row Echelon Form
Actually, we can do more. Continuing from the previous matrix {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}}, we already have

{{41c4b5ecd09ec024c5a08c58bf6790cc31bd55e5b285183e3a5564769ab5e6e6}}

We eliminate more, making all pivot columns left with only single one.  

{{f591e074d467e2b4f77b3ca63a39e0e49cdbc56c03399a8f68973f36ca7630cb}}

We call {{a28faf6143663643c867a9e6316c985e9cef6a6ed418572e97343866efcfe288}} **row reduced echelon form** of {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}}, denoted by {{115d4dca7f584c586474b5188ad609d598364a6ad7a917417cbfa01c6749771b}}.
The idea is when we are finding the way to balance out the effect by picking some free columns, we have to pick exactly negative amount of these pivot columns, and the solutions can be seen with ease by this way.  
Let's suppose {{a28faf6143663643c867a9e6316c985e9cef6a6ed418572e97343866efcfe288}} is in this form:

{{b43c886d424a0125f66d089bf9af9b354514131005673a54f63ae62c99dc14bc}}

Where {{4a1f941b3c6f426ec08de78c17e2f80f07a8b789701ba6b25126da00fab1231c}} are the pivot columns and {{ece49feba00b8a1812ded074f725361efa66b3c98a069a56aeb4b360bb7aee93}} are the free columns, then the null space of {{a28faf6143663643c867a9e6316c985e9cef6a6ed418572e97343866efcfe288}} is the column space of

{{e6411cfad4b7d9721f8bb4547bce0f6f88f1e49930040e1ce958b2dc12be4414}}


Another example, suppose {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} is

{{254ed300815accb2f4720ae961903afe774e30f89f5ed32a052b97b7d15861cd}}

Then we have 

{{809110451ade5f8f743f7fc4a0793a610bc83b2890c09a43e05bfbd83bb5ef9b}}

and also

{{15b3e38d2b4c53fd19a803358292a9d7105663e4909802185bee78d7c07c8f0a}}

The rank is {{b71be43b02045b8b4173d0bc2a348d09d5082ab0b79985e03def8bb55c796534}}, and there are going to be {{72bc3c1b3553a71d525d8715f4963adfb2b8e7e18c32f0b1b651f3e841526770}} free columns. The solutions are

{{9f16cd37feb740d8c61c7cfdc08f359d477e9d25255d40223f054d33c3dfa8d9}}

You see the formula we just obtained also works here.

\[Lecture 08 starts here]

#### Finding Solutions
We already solved all solutions of {{4074e034bbace4d58829fdf654eaa6b996d0026c30aadf3b9ce42f07b7fd9414}}, then what about the general problem: solving {{7a972db4806577ebad9da3316b822dc27b3282cc39e03983f6237922c19941e2}}?
What are the solutions? How many are them? Or do they even exist?
- Existence
	{{00511bf0a6978c2c0834726bdea81630ee1b0d33f80bc837d9bda37ad4212cd6}} has a solution if and only if the augmented matrix {{ad2981b908d1ddc20e81cb639f2ef1c2c2cc3bdcb192a279f869ba35545b6c4f}} does not have any row with all zeroes in {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} but non-zero in {{00511bf0a6978c2c0834726bdea81630ee1b0d33f80bc837d9bda37ad4212cd6}}.
- Uniqueness
	If {{00511bf0a6978c2c0834726bdea81630ee1b0d33f80bc837d9bda37ad4212cd6}} has a solution, then after elimination (into rref), we can obtain a solution {{ea64dbae195688eb6f0bbc6e40a85ebc7939b25e21f8f5d0ae506ad261a60105}} only using the pivot rows. The full solution to the equation {{7a972db4806577ebad9da3316b822dc27b3282cc39e03983f6237922c19941e2}} is every element in {{34e96ddb8fbc126c7741411e32d42999f8a5c4ea6dd5aae37e10c7a8547866fc}} where {{ed8bd9611d6a011f6c88848a5c7df96221f17694db98ad4f384e46c5840cf0f1}} is the null space.

Some special cases:
- Full row rank matrices {{cba39354af0e863545355befd3ec32c98ae3dfddc8d905d838d92c8004f9acd4}}
	Every {{00511bf0a6978c2c0834726bdea81630ee1b0d33f80bc837d9bda37ad4212cd6}} has a solution, and there are infinitely many solutions for every {{00511bf0a6978c2c0834726bdea81630ee1b0d33f80bc837d9bda37ad4212cd6}}.
- Full column rank matrices {{7c300ec9e4d0191b5f29c64afa8c608ccbc473cf775046f43028d3c4774be00b}}
	For every {{00511bf0a6978c2c0834726bdea81630ee1b0d33f80bc837d9bda37ad4212cd6}} has a solution, there is exactly one solution.
- Full rank matrices {{406ea1a8dfc9ed6acf088ff9bf9fbfa99965143e5681eb84d4a628d22ac8a913}}
	For every {{00511bf0a6978c2c0834726bdea81630ee1b0d33f80bc837d9bda37ad4212cd6}}, there is a unique solution. In other words, the matrix is invertible.

\[Lecture 09 starts here]

## Independence, span and basis

Suppose {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} is a {{cc09daba676fcefcfb20c1e9e42db1b746b5953e04532813493b40fb4841c60e}} by {{bb28a9b83048a0f36a72a56394914040f7f0171b49534f6138053bdd68916943}} matrix with {{0696c5921c7ca755c1efe29ff8008446fdbb6e7f565a58fd41d93ae1295068d8}}.  
Then there are non-zero solutions to {{4074e034bbace4d58829fdf654eaa6b996d0026c30aadf3b9ce42f07b7fd9414}}! (since there are always free variables).

### Independent
**Definition.** Vector {{4d719ba17cc043dc9d4dfcef2e75fb8f8f066b13554be8abb2bb91795de77b0c}} are called **`(linearly) independent** if no non-zero combination of them gives {{3c41ab82404b92ba66789b91a0708dfe8056842a6f99375e37641526f2eb3796}}. Otherwise, they are called **(linearly) dependent**.  

**Property.** Let {{4d719ba17cc043dc9d4dfcef2e75fb8f8f066b13554be8abb2bb91795de77b0c}} be the columns of {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}}. These vectors are independent if {{dfe7beab97813e9aadd298de97bbe1a7a682f92dffedaaaaf2af879a8b8396f6}}, which means {{e09a11be6ba512a859745c655162b4aac32b1986dff61ab4d83be284cc1f04d5}} and dependent if otherwise.  
It is easy to see that property is true.  

### Span
**Definition.** Vector {{4d719ba17cc043dc9d4dfcef2e75fb8f8f066b13554be8abb2bb91795de77b0c}} **span** a vector space which is the set of all linear combinations of the vectors.  

As column vectors, we can say if {{4d719ba17cc043dc9d4dfcef2e75fb8f8f066b13554be8abb2bb91795de77b0c}} are the columns of {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}}, then {{4d719ba17cc043dc9d4dfcef2e75fb8f8f066b13554be8abb2bb91795de77b0c}} span {{56d1910ade815ed546930d65d2ba35dcb0f4d29fb2cc8375c230ab262b0a2261}}.

### Basis
**Definition.** For a vector space {{da8c27c394be59d9d79201471429ba3328591059253284e430ee5c6965e2f2f9}}, {{4d719ba17cc043dc9d4dfcef2e75fb8f8f066b13554be8abb2bb91795de77b0c}} is called the **basis** of the space if
 1. {{4d719ba17cc043dc9d4dfcef2e75fb8f8f066b13554be8abb2bb91795de77b0c}} are independent.  
 2. {{4d719ba17cc043dc9d4dfcef2e75fb8f8f066b13554be8abb2bb91795de77b0c}} span {{da8c27c394be59d9d79201471429ba3328591059253284e430ee5c6965e2f2f9}}.  

Example. 
{{fe9761a0b212ecca4d02c7ba41c0cff7f8d84f321fd79e6888995763bddf6174}} span {{7f64273a25f8d804c2477f248d3b74e3ecd5104b7458bfb9caba04beae26bd10}}.

**Property.** {{bb28a9b83048a0f36a72a56394914040f7f0171b49534f6138053bdd68916943}} vectors gives a basis of the {{2e7e0fda85cbac2daa211d325a1df218b01b97af174187de478d433432ed2321}} matrix containing them as columns is **invertible**.  

### Dimension
**Property.** Every basis of the vector space has same number of vectors.  
*Proof.* Suppose a basis {{efb7e5c4b45399cbcd42becbbebef4cc92512f342936ec56f902ed1359b4a9bc}} is bigger than the other basis {{00511bf0a6978c2c0834726bdea81630ee1b0d33f80bc837d9bda37ad4212cd6}}, then we can know after elimination, {{efb7e5c4b45399cbcd42becbbebef4cc92512f342936ec56f902ed1359b4a9bc}} should have null space other than {{35d8163b91f01f05d585f13d8d5f91272ecb5556451f2e2cda079e0799d41fd3}}.  

Therefore we can now tell how *big* a vector space is.  
**Definition.** The dimension of a vector space, called {{44ff503c3d029a96c9aac1b1d165b9ebb84c4618b1a31b2c11af8ba8e797047b}}, is defined as the size of its basis.  
**Property.** {{becb59ae833e538f0f571f85d9d0f9f4695f6e35edac0b84638287e91efa8b62}}.

Keypoint: if you already know the dimension of {{da8c27c394be59d9d79201471429ba3328591059253284e430ee5c6965e2f2f9}}, then every independent {{44ff503c3d029a96c9aac1b1d165b9ebb84c4618b1a31b2c11af8ba8e797047b}} vectors in {{da8c27c394be59d9d79201471429ba3328591059253284e430ee5c6965e2f2f9}} is a basis.  

**Property.** Suppose {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} is a {{2e87ae438631ace8180e8ae97ee5c30a1e8913c8f68208d19b918f0230908a6b}} matrix. {{81bbee24edcf1accd0122427bb7a7e6d7604c84998696a0f6d9cc00489c4920b}}, {{2cce5369afa66ee8c391fabd70fc6c345c74cafc4f88898fb9f0e0f679d32e77}}.

\[Lecture 10 starts here]

## Four Important Spaces
Suppose {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} is a {{ea73d358ba1b17eb498e509f49b7a957e9198a895a025b974c63cb16d639e49e}} matrix.
 1. Column space {{02b3f9048a74a0d858b78f4fd88a7c87dc04036457df502d8483bf97c7feece0}}
 2. Null space {{80e24541ddbca8ea4d7f01f130464f7ccceb58f5c22f3f729740d71aee11bfc7}}
 3. Row space {{d650cec961934af7363e8258ff2bf433edde43db202a307bb6b3ecf21cfe63f7}}
 4. Left null space {{efb6e05435e229a92a28bc4669771381873144ba187ab39fce6f08fb49936506}}

We aleady know how to find the first two. What about the rest?

### Row space
We are interested in what vectors can these rows span?  
The idea is, **when applying row operations, the row space does not change**.  
Then we are just going to find the row reduced echelon form, and the non-zero rows form a basis.  

> The reason why this is correct.  
> All the zero rows was a linear combination of the rest before elimination. Thus if them remain, these row vectors are dependent, and we can delete them safely.  
> Also, we don't reduce the dimension of the row space. Think about it intuitively, if the rest are independent, then replace one as itself add others should not make the new vectors dependent.  

Say {{97797a6dcf9384b11850cd869d615e85c2f046ba57079d47f61e5ff0ab8a2b7e}}, then {{2e72af93c7f6b9be1e65bef2f2c2f9ec81b1cce4bd71847990acacf3f7e44f8f}}. Thus the row space has a basis of {{21fa94cf9c18b4198f205c7c200912ee085e1d849fe78f7ab270e5621e59934a}}.  

### Left null space
The reason it is called *left* null space is because, it contains all elements {{bead6513981f86c92c1b955f22650cf775ed108fa2975e5e5866501cd938a193}} satisfying

{{c5e303caef6a83c8ead4f6447172e196abd2023986958096bfaa31fcfa1f4f7a}}

Transpose both side yields

{{1835956eaff1854dd7b8597a68554cbf0d02ce9ff26bf82982cad19518909379}}

which resembles the definition of null space but the vector is on the left side.  

How do we find it? Well, now we are interested in **what linear combinations of rows gives a zero row**.  

We know they are going to be some (or none) after we reduce them into row reduced echelon form, but what are these? We need the elimination matrix.  
Let's use that augmented thing again.  

{{3583212173b921e29da7e7a84fdc21177a29f50607ef882ca148ab1342177e3e}}
  
Then we know for each zero row of {{a28faf6143663643c867a9e6316c985e9cef6a6ed418572e97343866efcfe288}}, the corresponding row of {{31757aae189f045a9c0f14808e2ab4d71c60816983154e31636799f537ff437d}} tells us what combination can we have this zero, and collecting all of them gives the left null space.  

For example, take {{97797a6dcf9384b11850cd869d615e85c2f046ba57079d47f61e5ff0ab8a2b7e}} again. {{31757aae189f045a9c0f14808e2ab4d71c60816983154e31636799f537ff437d}} is going to be {{a21a3d08e62fd6cf8044796463999eb045a8ee866bed65a30e0fcaa6f91f4c7e}}. Therefore the left null space has the basis of {{a897c9bdefe17ed26b8636bdc3eec41057fa2ee5f3e802784f8389a3e86843c6}}.  

### Dimension relation
The following relation holds:

{{59e066f9d6a1ec1ae85ddef7401b0ab2fe4ff990d1f99b5e668d1e9e9b14bcbf}}


{{6ef2d8eeeb716a40b0c509edbd2f2646c6d807a3946bfddacc72fa5c16a91b0b}}


{{5b23b96db90eaf1506a688b73aca1ecec731daef6b16faf337de4cd9c8614d46}}

The first two are pretty obvious according to the definition, and the last can be observed that the pivot columns have the same number of non-zero rows, thus they have the same dimension.  

\[Lecture 11 starts here]

### Other Spaces
Let {{29742240025756815de7b4dc24b2f1de69b9148b4ec37f961ccb4d9b4836ab30}} be the set of all {{d4c571db54e97c192459bcdb7395453d7414645b3a291bdcbea378637b00df20}} matrices. Is {{29742240025756815de7b4dc24b2f1de69b9148b4ec37f961ccb4d9b4836ab30}} a vector space? Yes.  
In fact there are several subspaces, such as {{77e20b8c0fd244389059c1bf04a3a6e065820ec77fa9ca323d829d6c5b908381}}, the set of all upper triangular matrices, and {{fdf30f5db1f3424874da244595a2db648c7b056dc537a2b62eb64b4d26d827ef}}, the set of all symmetric matrices.  

We know that {{78a19297d21c2856d3c37fe711972a88061f7a5ef9738769a0f82710fe7f8620}}, and there is more than that.  
Let {{8653fe6c8fab015a59b37c4736fe986a64a2be9fde30c908a98cb8ceaa2bc687}}, then {{3a16fddd1da7699eacf47cfa3f73a53f8176dd10cda11e68d6a4b5424b1c8285}} contains all diagonal matrices and {{41dd2f62a561d45fe4680e1fca46afdfbef8bdb472522be501f63e7e0cd1d26e}}.  
Let {{cb469ac97ed94da64bac2843485d72590e29332cd75468b1e562fa7b3cd65b4d}}, then {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} is {{29742240025756815de7b4dc24b2f1de69b9148b4ec37f961ccb4d9b4836ab30}} and {{df0676c81dbd8cc1daf0e6316398b89532106d75978e2dcb2eb3a2be2db16e2f}}.  
A cool relation is that, {{bfd071b94e9cda68a71c560ecfe2846e71047b7eb41446178bc54c8deafbf6f3}}. Is that always true?  

Another example: let {{fdf30f5db1f3424874da244595a2db648c7b056dc537a2b62eb64b4d26d827ef}} be all of the solutions {{bead6513981f86c92c1b955f22650cf775ed108fa2975e5e5866501cd938a193}} to the equation

{{486069ce3bcf80eba485c72cd5d7e10c580634a90ad181bb3edf36d4cd4f00e6}}


> In differential equations, we will know that the solution space has dimension {{b71be43b02045b8b4173d0bc2a348d09d5082ab0b79985e03def8bb55c796534}}. Now we assume that is true and think of it later in calculus class.  

There are two special solutions: {{0439677f51e73b151f71313630cc563b8a972c5552a9425a7c2e6a30477147a9}}.  
And they span the whole solution space {{fdf30f5db1f3424874da244595a2db648c7b056dc537a2b62eb64b4d26d827ef}}.

### Rank 1 matrices

Every rank 1 matrix can be expressed by a column matrix times a row matrix.  

> It is easy to see that: pick the first non-zero column and the first non-zero row, since its rank has to be 1 and all of the rows and columns must be some constant times a scalar.  

\[Lecture 12 starts here]

## Applications
### Graph Potential - Currents and Kirchhoff's Law
Graph is formed by a set of vertices and a set of edges, used to represent abstract idea of real world connection models. In this case, we are going to discuss **potential**, for example, electrical potential in circuit.  

Let's talk about this graph {{9f999f3336057a30ba88cfc952c6c77e5103882f11c7bdf1bbe13b4cba803242}}, it has {{a7e24f17d0d86903bbad9f8e532c9f0e236568c541c7d7b5797de6792e3c180b}} nodes and {{e09cabf12c713b88dfe8f1de4919d525f2b6dbcc4d59a1a9df2192af0b32fa8a}} edges.  

```
1--→4
|\  ↑
| \ |
↓  ↘|
2--→3
```

We define the **incidence matrix** {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} of the graph as a {{a6cb582a03221d0fc1798ee6e114cf9cc541a7e36d2a9df54af43616039459cf}} matrix, where each row represent a edge.  

{{9464639e39420003b4968d991b7311aec6d42170c2c79e32ab20c43bec352218}}


Why this is important? We will see a few applications.  

- Potentials  
  Let's say each vertex has its own *potential*. Therefore the difference of potential of each edge (which indicates how likely or how strong power is going down the edge), is the incidence matrix {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} multiplies the potential column matrix {{22bf003d6cac79e1d917cacdab9539c5d59468c02c22d29c08df00834ee4bbe6}}. In this example, it is
  
{{dc2749c5c75d51ac75595cebab6319658e95f5b03516bd1a78142fe7f555987c}}

  Solving {{4074e034bbace4d58829fdf654eaa6b996d0026c30aadf3b9ce42f07b7fd9414}} gives us some possiblilties of stable state. More specifically, the set of all stable states is the null space {{c9a8aaca1cb38b2096cb64ae8910310fd0c3774433afc7fdd5f1a663c5b13413}}. 
- Currents  
  In circuits, these edges are wires and some currents run through them. In this case, the potential of each node should have net difference of zero. Therefore it is stated by the equation  
  
{{bcd19738a44579b8387056b994b095f0931147cf4a541bc5415f9ff64534b6b4}}

  
{{e97a1aabe4a762ca60892207e0d88894742fe0aa94184b72870ec8f7aba80550}}

  Solving the left null space, {{13718300aa31bd2f5bba9315bfb059c466a3ce3592342f7eb444b7b6cc0fff62}}, tells us what are the stable states. In fact, the basis of the null space are *circuits* (or called *cycles*).  
  Assume the graph is *connected*, we have the following identity:
  
{{488b39fbe48974aabe89b3ff19a14c3b648261b8e0d10759120eadcec1b27b6c}}
 
  In physics, this is called **Kirchhoff's Current Law**.  

Using Ohm's Law, the two aspects of incidence matrix can be united into a single equation.  

\[Lecture 13 is about Quiz 1]  
\[Lecture 14 starts here]

## Orthogonality

Two column matrices {{8fc048119806a725cffe1e19d527734d62ce724b5cc279975e835655b1c51337}} are called **orthogonal** ({{15ec2becb22e447ad3ead863609658f2bd6a54fa211c342dec95af9da99b83ea}}) if

{{3597d4e315eafe0a512cf90fff8c286d3a4d65fda5c81e064cb8d467d78918cd}}


**Property.** Let {{9885251f704c9a585f5b1d5025f6f36e8a180dc544748f0e001bc93aff67ee06}}. {{22bf003d6cac79e1d917cacdab9539c5d59468c02c22d29c08df00834ee4bbe6}} and {{bead6513981f86c92c1b955f22650cf775ed108fa2975e5e5866501cd938a193}} are orthogonal if and only if

{{b992d805b37786364a7fb3c5ac4de5636a36ec10c3de595118ae3c2991643436}}

*Proof.* Expand RHS gives 

{{73ebc82c665ee14748928ae9adf79dd3a64348430b116effe4e49297f5fc876a}}


**Definition.** Subspace {{fdf30f5db1f3424874da244595a2db648c7b056dc537a2b62eb64b4d26d827ef}} is called **orthogonal to** subspace {{cd15d3a571b67c26cfa4d135c0beb323c631d85844625699d123761440301d5d}} if 

{{b42f8df1b136a192393f5260c6d3c4ec112debe5362f3436796a0c471f630727}}


For example,  
**Property.** For the same matrix {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}}, row space is orthogonal to the null space.  
*Proof.* Recall the definition of null space:

{{654907265c1c379feee66adc7d97b8e497e36675894d8d591f98fe01b2046702}}

Thus for every row {{a924f6a91c6957d048bf210baea8dfe7727f90c8cd1a215285ee0fb22cfb169c}} and every element {{22bf003d6cac79e1d917cacdab9539c5d59468c02c22d29c08df00834ee4bbe6}} in the null space, we have
{{6237210e3d6e7192894ca86edd10546707af6ddd98176e8d67c55918a25a75cb}}
Since row space only contains linear combinations of the rows, they all satisfy the condition.  
Formally, let's say {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} is {{ea73d358ba1b17eb498e509f49b7a957e9198a895a025b974c63cb16d639e49e}}, and we denote row {{566ce35497d2b07c5147093d9ed70d8e54fdfbb259f9ad5d2607533994a1a6d8}} by vector {{a40ac0185e32fde04bf6a9f41676f745a22d70d99f7014494bedc8f6f829ae9e}}. For each element {{ac74c8ff1716f28b1cdfcb945b9b3e7486cf40a1f770eb9dd1838059b64ad8f4}} in the row space, we can find {{cc09daba676fcefcfb20c1e9e42db1b746b5953e04532813493b40fb4841c60e}} real numbers {{cd2b200d8cdbc382036dd7e3b0f9f9012bd397992bb60750d1fae432ed9a3670}} satisfying

{{d242a06876d97d544759cdbab035e64714d9689061dbae316584f1f25b9a9b54}}

Therefore, for any element {{22bf003d6cac79e1d917cacdab9539c5d59468c02c22d29c08df00834ee4bbe6}} in the null space,

{{da619bc8ea7d6e8fb93e7ff47e30e70aafa4fa4817fa56e752b0569bb26944b4}}

For the same reason, column space is orthogonal to the left null space.  

Not only they are orthogonal, they are *orthogonal complements* in {{0d34742bc8eaac8129622066a94d8759199ce89b472a10ddcbfde47aa8e40fe9}}, which means null space contains *all* vectors that are orthogonal to the (all the elements in) the row space and vice versa.  

\[Lecture 15 starts here]
## Projection
### Motivation
Using the knowkledge we've know so far, it is possible that

{{4e550e38612e960a580687d52035bda104c6e89c4429b15e764328825650605a}}

does not have a solution, and it is bugging.  
Sometimes we want something that is *the nearest* solvable {{00511bf0a6978c2c0834726bdea81630ee1b0d33f80bc837d9bda37ad4212cd6}}. For example, we want to find a line through {{6eb60d64f8113a7cce51be0fbcfa887fe2aec1d86ed1455804835b2f70e8568d}}, but it is certainly impossible. Then we start to think, if we are going to find a line that is closest to the ideal one, what would it be?  
It turns out we want to solve it as

{{8c9bbb4d0af4f5f386900e8900e73f7e694d01dcc355b3537a3a8fc2ff2e516a}}

but as we can see it has no solution.  
Projection, is the tool that enables us project any {{00511bf0a6978c2c0834726bdea81630ee1b0d33f80bc837d9bda37ad4212cd6}} onto the {{56d1910ade815ed546930d65d2ba35dcb0f4d29fb2cc8375c230ab262b0a2261}} in a formulated manner, and it is invented to solve many problems, including this one.  

### Projections onto Subspaces
#### 2D cases
Let's say {{0923f3defb8f13e1638ef4a4115b9877e8e1a1109d1b3593cb5a8f1e2ad162f8}} are two vectors. What does it mean to *project* {{00511bf0a6978c2c0834726bdea81630ee1b0d33f80bc837d9bda37ad4212cd6}} onto {{401c22f57c1a7b3fd9bfbab993a1217702bf668f556921022a06b811573d8f24}}?  
We want to find some {{9bc8c334dabfc06a6528d0f5cb57090d3015fd84582b97d480a1a4fb46455bcc}}, and the error {{c83a56e346da550ac32ca6593c3b5c91a6efaa7189e5a5643d78540a8279d1d9}}, should perpendicular (or *orthogonal*) to {{401c22f57c1a7b3fd9bfbab993a1217702bf668f556921022a06b811573d8f24}}. In the language of math, 

{{f7b7f498898814e4d6af97a7f14fdaefaa27422c3d2a96a09d38736b5a0fb6ea}}

Solving it yields

{{04419b760d19b70996a752e5080c07caf55077258676db50b05f145f468ab42e}}

There is something noteworthy, that is, if we re-write the equation as

{{a54a0a6fb176ba9ba5f2d1f74c9e7d16153e4d9552609450f5eb822b87be6b1a}}

This gives a matrix {{af1a2d80b3e094b72596cc2accad35801d4606e28a361e5b4baae56bf8d66ea8}} which does the projection work!
Also we have the following identity:  
**Property.** Assume {{83e05657563b28cf0b63748e1c794cad196c106a2c5499d9fa561d9a35e7f865}} is a projection matrix, then  
1. {{83e05657563b28cf0b63748e1c794cad196c106a2c5499d9fa561d9a35e7f865}} is symmetric.  
2. {{cca3f540a81555de268644ed4668cd6891393179a2d3d3656e32ab54e4d84345}}.  
3. {{5776f410e6a31bfc0f6317c4436738b3de8d373bc3325622e97cd24241f03226}} if {{2d7319cffeb5c3def424b874e1c69a126e456c8892c3af4a33eccfb582e9fa95}}

*Proof.* 
1. {{585e7ff75eaf36fa38ad67a20dad1d26181e6d5e72bbdb9ddb9510e826648a4e}}
2. In geometric perspective, projecting a vector twice does the same thing of projecing it once. In explicit definition,
   {{ede269d140a3da58a2a9cd6bd3c33a9fb42dc6f35219df45f12704aa6e3877f9}}  
3. It is pretty obvious by the definition: every row is a multiple of {{1a205616e9d3d65dda5aed209db4ba2cd4246e857caf58d271d9893a857aa447}}. Moreover, {{8913f595d73e18ba6581286dbad732bf8f170b7c20e8e469087b763852406c46}}.  

#### 3D cases
Let's say there are two vectors {{915258f5fac08365dd67f5acaf3b51604b41f0e564c3015c592daa5c9fcc550f}} and they form a plane. How do we project any {{00511bf0a6978c2c0834726bdea81630ee1b0d33f80bc837d9bda37ad4212cd6}} onto the plane?  
We want to find some {{ea6649a9e145c333693e04f2dfe6435ea3f67511edf186c7d4e9dc63058f446e}} which is the linear combination of {{1d315ce47d3a5a2e9811ee0592688399fed9aede306b4b9919c445e7a57edf97}} and {{7b522120da08ee4563ff45041d038edaa7e97300261bf658e8feabf1aa53c186}}, and the error {{c83a56e346da550ac32ca6593c3b5c91a6efaa7189e5a5643d78540a8279d1d9}}, should perpendicular (or *orthogonal*) to {{1d315ce47d3a5a2e9811ee0592688399fed9aede306b4b9919c445e7a57edf97}} and {{7b522120da08ee4563ff45041d038edaa7e97300261bf658e8feabf1aa53c186}}. In the language of math, let

{{c06439f5390906d393e5d252a112e5cadd2fb4e06ed143217f673006f5fbb49f}}

we could re-write that as

{{531b85749d856c2b32c975f6a9b48091bb2f888c9ad100913ddd654b82e524cc}}


{{7c7c4c32451df1500252fdb61221fda74e58669396a33186ff70fd63ce3e9609}}

In matrix form, 

{{c229fe9c069ce0d75f1de5eff41273c608efa2c8c989513c5d238ce65f199e4e}}


{{506f42ec88063b4b07393c51ece8b69eaba37f4c458a6e77a4fc7b67dd91b4de}}

Notice that the error {{e092a424c94851fc0369aaa75728cd4b0aab6ae5781754192557cd09ef5ff08f}} is in {{13718300aa31bd2f5bba9315bfb059c466a3ce3592342f7eb444b7b6cc0fff62}} (which is kind of intuitive: we restrict it to perpendicular to the column space).  
If the inverse of {{0533361c09337ae0e1b6248facccbfe114d9fe65d710d21295fa24a3bcb6ea60}} exists, then we can find

{{ca0d505b03142f3c4f6659e04329bce4479c08bf0c774db6e34605598f38bca0}}


\[Lecture 16 starts here]

What is happening in the projection matrix {{6ccbe8326fc31d124a6b54a8e0bf136c3a65bb7a450652911f6f87280a277f59}}?
 - If {{00511bf0a6978c2c0834726bdea81630ee1b0d33f80bc837d9bda37ad4212cd6}} is orthogonal to the column space, then {{2a744854f06f9e606f143c5be1b68f71e8b99708ed348e28a556e944d8b58d3d}}, giving {{00105b68389803bead32ec7183b592e97a1bec306d7aef2f411f1d987dac3a06}}.  
 - If {{00511bf0a6978c2c0834726bdea81630ee1b0d33f80bc837d9bda37ad4212cd6}} is in the column space, then there exists {{7a972db4806577ebad9da3316b822dc27b3282cc39e03983f6237922c19941e2}}, then {{f3c05a4c6285ec7cdbdad39e8039fb9e983014fc56571951ae2169f3f40fb5d2}}.  

We can see that we are actually finding two projections: {{2651a09ac5fedc8b78fd6149a8d3b27969058f41aecdcb5cc2a4bc8a66c5ba77}} and {{1c59da211ea8b7d49a1231836618a741c384e0ad9ea2e4843f083dd9c95a1449}}.  

**Property.** If {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} has independent columns, then {{84eaf0a72edd42856d9595cbdbc0df0181e6d8880ad62f54ea8bc81729548e90}} is invertible.  
*Proof.* Suppose {{8db02ded11ded46ebeea6bd4d11e7cadd110b69a72593ab11ff25960c4ddbf4a}}, then we want to show that {{28366fab2f419c0d05de5339bdb57fe8aff8dce4e6d171cd91675b0271548a66}}.  
BRILLIANT IDEA: multiply both side by {{0a8625fcde7a2b1d147e4b47131b3c3a4bc33db2ba3d84fb846d998e3e4f70e6}} on the left.  

{{101820c7b9eea429430b29d8ec2c228f10b52637093c1768eb0b1f3dc4840f52}}

Therefore 

{{3898fc21174f16b49e07bf10959253d92c30ce58b2f8d48443d2b7aac290b5b8}}

Since {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} has independent columns, its null space is {{35d8163b91f01f05d585f13d8d5f91272ecb5556451f2e2cda079e0799d41fd3}}. Thus {{28366fab2f419c0d05de5339bdb57fe8aff8dce4e6d171cd91675b0271548a66}}.  

### Application - Smallest Square
Let's head back the example we left as describing why projection is important and actually solve it.  

**Property.** If {{2651a09ac5fedc8b78fd6149a8d3b27969058f41aecdcb5cc2a4bc8a66c5ba77}} and {{89a98293ef59faa8b18f83da400869714050e39cd87596262108ba89da2a018b}}, then {{11510e9ccde57f116493dd3ce3ac86e340a96a180478d506e135b9805abc0d61}} attains its minimum length ({{ec9932a666c86adeb1d2e4a6268fab676e4b6561b50bf82b6b1fd1324e06b36e}}) if {{536c1deaf5ab431ede52e2997394cddaa927f087450cbe493c64b8e16bdc49ab}}.  
It is kind of intuitive, if {{11510e9ccde57f116493dd3ce3ac86e340a96a180478d506e135b9805abc0d61}} is not then we can always extract the part in column space and get a smaller one.  

In 2D, we are going to find a line {{9f884dceface6d8b10961f5b83e8122b50f1fbfa701e09370c36aa551d6978e8}} to make the error as small as possible. The points were {{6eb60d64f8113a7cce51be0fbcfa887fe2aec1d86ed1455804835b2f70e8568d}}, thus

{{8c9bbb4d0af4f5f386900e8900e73f7e694d01dcc355b3537a3a8fc2ff2e516a}}

and to solve it to the best,

{{f3d8552c32f1077ca6f07d2de90cf19be52d85bb18967cbd6a302e59150cb212}}


{{8a851911d7e726686f41946895535d8f3173f389bbb911f416c58b951913e73e}}

which gives {{c4a6e88baa4bbd7f8928506092f327e602c5d362f68bf9b4b4f5e31b6c85c693}}.  

> There is another calculus approach: since the least square is a quadratic function, taking its (partial) derivative is not a hard work.  

\[Lecture 17 starts here]

### Orthonormal basis and matrix
A basis {{a7690f5bdfd05a5818ffc83b4ddff903e6b1c096d9fee9e49d0b4ff406b629d8}} is called a **orthonormal basis** if {{441b991bde0222288a0dd47549784f1c52ae5b2cd2c1f86e7a14f11deeca6ade}}.  
A **square** matrix is **orthonormal (orthogonal)** if its columns are orthonormal basis.  

**Property.** Let {{2d71baee65a33d7bf4a8aff45e1eaa40b228c18e97befd6644a813e6a04047fc}} be a orthonormal basis, and {{b525ff417c068f70299f711fe1a315f52a9e04e3fa2d0379b19230443ab40b6a}}, then {{4084f73535a2c0bcce6ada342f27f42ec93ae995b8189e02dc5c301ba45b4b98}}.  
**Property.** Let {{dd11800f714369a3bc85b47336b772601d1cd08bd1945d0626f6cc34e3274499}} be a orthonormal matrix, then {{97a63df517fa2bbd54803d96f01c337f71e94d9eb13bcb99638caef2b1cd92cf}}.

Why are we discussing orthonormal basis? It turns out when dealing with projections,  

{{2ef066cb3e91fd19cf580751d5f4c72a241f8dfbb438dd22353971ebd60b1e0a}}


{{24d6f5c6e0f642938f0c97ef1341779a0b450b7a2127b52bd59dbd1d89c1305b}}

If we could, somehow turn every matrix {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} into orthonomal basis {{dd11800f714369a3bc85b47336b772601d1cd08bd1945d0626f6cc34e3274499}}, then projection is very easy.  

### Gram-Schmidt Process
Goal: turn every matrix {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} whose columns are independent into matrix {{dd11800f714369a3bc85b47336b772601d1cd08bd1945d0626f6cc34e3274499}} formed by orthonormal column vectors.  
Idea: The first vector can stay, and for each new vector we meet, we subtract its projection to every previous vector. Finally, divide every vector by their length.  

Suppose we have {{a2a371dd5c59908a5bc73e8dc443b0172a096a5212473494b9cb9ae959804b5c}}.  
 - {{ff5bf6611ffd38c9f511c7850c96d97295b81ab02aa4394a1d2fbd338be53ba9}}
 - {{ab320b394c20352d3cadb3fc666fddf9ea4acf253d3d10998bc2ea0ea0f786c1}}  
 - {{2a918f76ed7ad2c4a783379d2f688fcad2364684bdd1a05333e5213d93a427ca}}  

Then {{1d433a150b9813ead749dde8867121bd21c8091611ca724e3fa93e005bb8bb85}}.  

\[Lecture 18 starts here]

## Determinant

For every **square** matrix {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}}, we denote its **determinant** as {{380654258bbf25141939816740e339e071cfc778efeb4fc199ebcb40929cf6e5}} or {{2540806a1758b22e0d7ac79d01f97e623d55956eb44c12ce4bd3c51c0cc00a38}}.  

There are 11 basic properties of determinant, and the first four of them (is one way to) give the explicit definition of determinant.  

1. {{2be1b32a3adfb2934b09d856881b59dde448301bfca8fd3a9f948670716e340a}}.  
2. Exchanging two different rows of {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} multiplies its determinant by {{65522b2d8a3a49b6a03dca589eb6295e7fcbbec0a570c4bc089fb058bdf355a4}}. 
   > It is not clear that every *permuting* operation gives the same {{3f2399f5234741f57f612b03218b4af2a2ee8efeb35a292ae2e14cb74df80e1a}} by any swap order, but in fact we have this property:  
   > Define *inversions of a permutation* be the number such that {{e525fdf129438b178ea027f87a2c448e7e331441c360fa7a49d29644293534d1}} but {{e351d716489480a632e09107e7ff1228441b71b5f5e414d329a30ade8e2ab7de}}, then whenever we swap two different elements, the parity of number of inversions changes.  
   > Therefore if we think it as the parity of inversions, every permuting operation gives {{3f2399f5234741f57f612b03218b4af2a2ee8efeb35a292ae2e14cb74df80e1a}} no matter how one performs the swap.  
3. Multipling a row by {{5568a4aa4ef3108c8947e1f3c6a7015eb309d3c080f9e4d6b253ae763b45f858}} multiplies its determinant by {{5568a4aa4ef3108c8947e1f3c6a7015eb309d3c080f9e4d6b253ae763b45f858}}.  
4. If two matrices {{6af9626098a21e2d9b65d2f645788d82f71da73b71aff63bc3ec8ab956352bc9}} only differ by 1 row, then matrix {{2a6f81ee63754c7772494d0f9901d5bdfb837dc7cd3bc5eff66467bd08dee26f}} obtained by copying other rows but adding up the different row has {{350536bd1503cbebe40f998b7ba11ef07acd5eb1f983d18c9a170f7a48c13740}}.  
5. If matrix {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} has two same row then {{e2927ee46ccc06a060caf21358953ba0e480c6dfccb70355fcd30bc9ad057743}}.  
   *Proof.* If we swap the two rows, we have {{4093927dfb95836c4b62d92323a8a321bb17feadd8856497fb0d95c900e559c5}}.  
6. Subtracting {{5568a4aa4ef3108c8947e1f3c6a7015eb309d3c080f9e4d6b253ae763b45f858}} times row {{566ce35497d2b07c5147093d9ed70d8e54fdfbb259f9ad5d2607533994a1a6d8}} to row {{27c5fdea0894415e9af99f00ea9e5e6438cea043c4715982465fd9d85b6185f6}} (with {{88cbb425c3835d8256e1e9f0e6d18d8f31e3b3048459bb7c8207564acab4dcfd}}) does not change the determinant.  
   *Proof.* According to 4. we can break the row apart, and extract {{1ced4465931d9220a1e5c7978c39b68942d771c7be3b11082c1e2af3639e4d93}} from the matrix conatining the subtract operation, which gives determinant {{04059783893b129d925417c55e95e559c8d4be599ebd2ca55aa2472bc9007f90}}. Therefore the determinant does not change.  
7. If matrix {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} has a row of zero then {{e2927ee46ccc06a060caf21358953ba0e480c6dfccb70355fcd30bc9ad057743}}.  
   *Proof.* We add any row to the zero row, and according to 5., {{e2927ee46ccc06a060caf21358953ba0e480c6dfccb70355fcd30bc9ad057743}}.  
8. For some upper-triangular matrix {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} with {{8859c4f7a286e6536c213234b3dd6afe40ae4a9d2933eeeef9fdc5bb528e1307}} on its main diagonal, then {{fdbb7de367df5b69252b51552c31279f2ea8810f6badd5153f1ce5b93175a23e}}.  
   *Proof.* According to 6. we can eliminate all elements not on the main diagonal, therefore we can compute that according to 3.  
   The same holds for lower-triangular, so an efficient way to compute determinant is by {{f100e37d91f6e265d274e59215e069feadc6b6335d7fe64185cf270e21468804}}-decomposition and calculating the determainant by multiplying numbers on the diagonal.  
9. {{e2927ee46ccc06a060caf21358953ba0e480c6dfccb70355fcd30bc9ad057743}} if {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} is singular; {{3fe38a6a411940a6e63fc61ffcd6f932c8e146d186854348a13b75a61bff4543}} if {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} is invertible.  
   *Proof.* With 6. we can do elimination and this property is pretty obvious.  
10. {{599701d90016d317e796f965de22f1369487bd3dce2c933107699b0e49df4c7d}}.
11. {{4cc08b90231f90a778ebfb939c56c9debd4e05cf65446edf06df4f97a785aafb}}.
    *Proof.* If {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} is singular then both sides are {{04059783893b129d925417c55e95e559c8d4be599ebd2ca55aa2472bc9007f90}}. Otherwise let {{f6072922cf82b2d6f835d02eecad5abcfafdcb551cb16a56875400f9ca3afbeb}}, then {{7405f4a3e28b847f7ffed64af4c63eeb2af50b453828a04122c49edec2acd9a2}} and it is obvious that {{10aa95b9b1db0f5dda67ea449d5fe0cd0bdfaf05531612605954609d6949a85d}}.  

\[Lecture 19 starts here]

### The Big Formula
From property 4, we can break the matrix into multiple parts:

{{257c2f89f8e27eb7fb3eead8d6947b2848c27ae06c4670aa28720dff71a46062}}

There will be {{9b057d0eb870f304a328c1178bec1b7b36259e6b47580321a5777180762f1103}} parts, but only those with non-zero columns will give a non-zero determinant, therefore we are left with {{354f2cd33016b72e9e45dcbff56978d3b45e8fc4b68e41a581e7fa341676009b}} parts. In {{f31358fe2adf9cd80df4e46ea73ec37b26c910121cfff44eec51b55135f9f041}},

{{fb5f9c19d4abde9778e447def6e666c645eb699979e06ec164fbe43caab23637}}


We can obtain the general formula by

{{17ccbc806a96631a15d4b5f8756e2a9587eda8d60cd2b8d40eb7bea3cf8dbaba}}


### Cofactors
There is a way to simplify the matrix. Take {{d4c571db54e97c192459bcdb7395453d7414645b3a291bdcbea378637b00df20}} as an example:

{{2ebcc32504d601e0ab05da031942a2b10d090fc15986727ee779b0aa84482c40}}


Let {{c4917c1e5c4c925031e648210dba8c21e026c53e4cc32eed0d08d6916783e9bf}} is the matrix obtained by erasing row {{401c22f57c1a7b3fd9bfbab993a1217702bf668f556921022a06b811573d8f24}} and column {{00511bf0a6978c2c0834726bdea81630ee1b0d33f80bc837d9bda37ad4212cd6}} from {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}}.   
We can rewrite the big formula of {{2e7e0fda85cbac2daa211d325a1df218b01b97af174187de478d433432ed2321}} matrix to this:

{{980d4cea3fb1a3e0e716186a479a07d24acb05b35c43bb4c737d51b4b69e399c}}


Moreover, instead of expanding by row {{72bc3c1b3553a71d525d8715f4963adfb2b8e7e18c32f0b1b651f3e841526770}}, we can do that for any row {{566ce35497d2b07c5147093d9ed70d8e54fdfbb259f9ad5d2607533994a1a6d8}}:

{{b4588d682528e2b5641397e76054f6c2c39cd85bf8ab8cceede162c2662f53a5}}

> The reason the sign is {{d2b6c6b87bb9416fc4b538b53a08b68e74f28b8729167a91a298b1dbe91bb62e}} is actually *how the parity of inversion will change if we insert {{566ce35497d2b07c5147093d9ed70d8e54fdfbb259f9ad5d2607533994a1a6d8}} into position {{27c5fdea0894415e9af99f00ea9e5e6438cea043c4715982465fd9d85b6185f6}}*.  
> Assume there are {{2725b2d0fc640cb2728a1834f8c41d47e601a7313494a3c35628268f485f3a5f}} numbers that are greater than {{566ce35497d2b07c5147093d9ed70d8e54fdfbb259f9ad5d2607533994a1a6d8}} in position {{72bc3c1b3553a71d525d8715f4963adfb2b8e7e18c32f0b1b651f3e841526770}} to {{ea933f69bfbcd8ee3292553ee2b624fb1b0646ce84f3350e1406749e2847a167}}, then the inversion is going to increase by
> 
{{233b61f3f90ad80184e8f0846b17c50c70c9c24f15d0baee1bdc3603fe87e290}}

> and it is equivlant to {{99148e8605dcfae03dbd03a26f76610fb1177211487b1241b9ff90ff69cf2ce4}} modulo {{b71be43b02045b8b4173d0bc2a348d09d5082ab0b79985e03def8bb55c796534}}.  

This formula is useful for some matrices where most of one row is zero. For example the tridiagonal matrix:

{{8c3cb684e6be6dfd1059ed86e93294ac38a352df13270f2b8c59b4d7c436e9b6}}

We have

{{bc42f04331bb2ac3286475ea12f24de0003ccae5b7d1e845812637e5f9b20b33}}


{{282b9dee215f3a29b33e2848d314f91256b962035746c74b8180ccf018570519}}


{{a1c9b2c90d61118465cbd3ec9245f62600de483964c5bf468c1f65ed2a2794d8}}


\[Lecture 20 starts here]

### Inverse Formula
Let the cofactor matrix {{2a6f81ee63754c7772494d0f9901d5bdfb837dc7cd3bc5eff66467bd08dee26f}} be {{0976974dad7e126e1537f52903816e65eec0d750e7517f05e517da4925720038}}.  
The inverse of {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} is 

{{86f6dc90ef4e6be44ef2f00448dc2baf0b3f8bebbaac5040c32d60d56354ce47}}

Why?
For the main diagaonal of row {{566ce35497d2b07c5147093d9ed70d8e54fdfbb259f9ad5d2607533994a1a6d8}},

{{f5b7d9cad915584daf87ca0aa433a3fe20ae9c4de333eee57b1f41a8b357594c}}

For the rest, say row {{566ce35497d2b07c5147093d9ed70d8e54fdfbb259f9ad5d2607533994a1a6d8}} column {{27c5fdea0894415e9af99f00ea9e5e6438cea043c4715982465fd9d85b6185f6}},

{{c1279e783a52ed9bef7395dc3ac91f680e9fd33e7b60a6fd9c682232edfa8520}}

we rebuild a matrix {{68e2c657635f73c4dcb5d524f457fd7522045402f0f6ff9d2e28879de6c7e67b}} the same with {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} but the row {{27c5fdea0894415e9af99f00ea9e5e6438cea043c4715982465fd9d85b6185f6}} is replaced by row {{566ce35497d2b07c5147093d9ed70d8e54fdfbb259f9ad5d2607533994a1a6d8}}, then this matrix is singular and {{f00b9f825d2a2418de5063e082199b7bef8ff1c2fe4ff7acf2bf79807d087e1f}}.  
Therefore {{099115f11054d3893509961c125364167b3feb38be15245005a2eaf31b88f75c}}, {{53aeff340106a81700887c9e20b4d4f69c97c1897649b87b1c8d4c0e1b369159}}.  

### Cramer's Rule
If {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} is invertible then

{{3c86bf23b37a0a8dceaf220064adc935a5e5e99e88cb9483d750db4330fdf42a}}

What is {{2c816a889b8bfc4563c5cd36d6ff461dc165d5b66864a889502b44bd0a72398b}}?

{{81682c74af29423cfd6ec820f6e223894ec0a5585b3bcf8a614fadd4b3aed893}}

If we define the matrix {{b60a35d63c8066418cf87b6f477182a4bdee695921b53518830572b137a00d0d}} the same with {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} but the column {{566ce35497d2b07c5147093d9ed70d8e54fdfbb259f9ad5d2607533994a1a6d8}} is replaced by {{00511bf0a6978c2c0834726bdea81630ee1b0d33f80bc837d9bda37ad4212cd6}}, then

{{7578135b2d2085fefed83aa629811b6a447dc64314a55638349d66954ebfb1e3}}

In general, Cramer's rule is a disastrous mess (since determinant computation is awful, the best way to do that is probably elimination). However it sure has some value, for example this is the *algebraic* form of the solution instead of doing some algorithms.  

### Volumes
**Property.** The volume defined by the {{bb28a9b83048a0f36a72a56394914040f7f0171b49534f6138053bdd68916943}} row vectors of {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} is {{db78306830316a137ee3e943a6fdcfe8279eff6b5e4459a0d417d51a35ae71a9}}.  
*Proof.*  
1. {{2be1b32a3adfb2934b09d856881b59dde448301bfca8fd3a9f948670716e340a}} and the volume defined by these vector is indeed {{72bc3c1b3553a71d525d8715f4963adfb2b8e7e18c32f0b1b651f3e841526770}}.
2. By definition, it is true.  
3. If we stretch any vector by scalar {{5568a4aa4ef3108c8947e1f3c6a7015eb309d3c080f9e4d6b253ae763b45f858}}, the volume multiplies by {{1bfa691a05fb90545908ef89761e7b908261b9527a3d6740644fde61052e8f1e}}.  
4. Assume the two vector are {{a924f6a91c6957d048bf210baea8dfe7727f90c8cd1a215285ee0fb22cfb169c}} and {{ac74c8ff1716f28b1cdfcb945b9b3e7486cf40a1f770eb9dd1838059b64ad8f4}}, let the rest vector form the base, then we are going to consider the height (i.e. the projection error {{11510e9ccde57f116493dd3ce3ac86e340a96a180478d506e135b9805abc0d61}}), and this projection is linear so the same property holds for both determinant and volume.  

Another way to see this is directly by Gram-Schmidt process. The volume defined by these orthogonal vectors are intuitive.  

*Special Case.* The signed area of triangle with corners {{dce1f217412635cdf849e8abe7305202c9d18652d896e8c9c4b8ff8b7bd2d68d}} is 

{{b64016102591bb488c0e39535f3f821ec5128ce4eef6946326dc99781e91a442}}


\[Lecture 21 starts here]

## Eigenvalues and Eigenvectors
**Definition.** The **eigenvectors** of a square matrix {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} is the non-zero vectors satisfying

{{cc3b1ea48401ad535cf63ed1a30ed941c0a6d763affbbea855f439e80091a197}}

for some {{31d61dcfe4a7b3caf3b8e9f71233691895a73b13a8348a69deba82518720e180}}. Here, {{31d61dcfe4a7b3caf3b8e9f71233691895a73b13a8348a69deba82518720e180}} is called the **eigenvalue**.  

We don't know anything about that, but here is a cool thing:

{{8d5d77b2726f1ceb6b49277a74afe125e49e98e7185c037b9e0683c28df81186}}

Let's see some instances of eigenvalues and eigenvectors.  

For projection matrix {{83e05657563b28cf0b63748e1c794cad196c106a2c5499d9fa561d9a35e7f865}}, if {{22bf003d6cac79e1d917cacdab9539c5d59468c02c22d29c08df00834ee4bbe6}} is aleady in the column space {{56d1910ade815ed546930d65d2ba35dcb0f4d29fb2cc8375c230ab262b0a2261}} then {{db060191025263a869b765f732bd2590c82a494f13fd7c82b2930d4ab94d523e}} and {{22bf003d6cac79e1d917cacdab9539c5d59468c02c22d29c08df00834ee4bbe6}} is an eigenvector with {{c70c0090f5ffc713fbf86bbb5bfc70057d79ec8ad1d211334449a1a662d6e785}}; if {{22bf003d6cac79e1d917cacdab9539c5d59468c02c22d29c08df00834ee4bbe6}} is perpendicular to {{56d1910ade815ed546930d65d2ba35dcb0f4d29fb2cc8375c230ab262b0a2261}} then {{410756c6a5ced16898a9af065dda3e6ebc27c516ee769123a0a4159d6bd4aa7d}} and {{22bf003d6cac79e1d917cacdab9539c5d59468c02c22d29c08df00834ee4bbe6}} is an eignenvector with {{22c7635c62a486acfc7888ce65aca3f5930231cd2e4fd85a7683756bdd82a281}}.  

For {{2b982f02af3251bab58e842c912a3a0c6b562a38584654565ab2059e53a13a66}}, we have {{afb99947b4bab3cdff7e35b6f19547942c4c770b76c6d3a4f67ef4db5fc822a9}} and {{8df1673032414d37b52e334a1f4671f4f12a46bdb49e059d1a3bcf1dd15405b6}}.  

For {{50c72ef8494f7f88d4b6be741039ef5f32412d3c0f524b35a88322f923a942f1}}, 

{{c1690ec8520f688969fc0df5c31869339f33e9e7ef046401c4d0b948fe6c354a}}

{{fc926e2e053094d12274eaf384571f89d7737076907413559e8f11638b360c53}} is in {{21aa32d1746453d589f539b48aa89a20bb1519d955357faf756c821b3ec42a66}}, {{fed3e5192b97be5d8a82907f3b0b6cb5ddc0a02db390ef8ca03c68d1482e4b3b}} is in {{5e59d839f864809651ecd952f3a984d80ed5a77771ae3a183a54f78da27ecba8}}.

For {{dd8f63c99ff9a2a5f342d9c243fd29ff13d884f84d0328bf93766423465f83b1}} which rotates any vector by 90 degree counterclockwise, things are getting strange: what the hell vector is going to have the same direction when rotated by 90 degree?  

{{a2ae82b43ccd7b3a6326b18bed60c638bf8ef8d57d151d5e872639c43e6e93c7}}

WHAT?  
It turns out the eigenvalues can be *complex* even when {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} is a real value matrix.  
> This is why the lecturer told "it was a disaster" since imaginary number were not invented until 1804.  

For {{7533aa457126c872924fa4a50eb9adfaeed8fabe15ebf22f537f2d638f17d0d3}},

{{25a58262fe874c02ea804d784972b3cda6e6df6ab221fe9f2c08559c3748fb0a}}

but the thing is there is only one eigenvector: {{8e41e0569ca1159fd8604849fcdafe9c9fd6c5a835ef601fd2654e02bcea0b2c}}.

It is noteworthy that eigenvalues are **not additive (linear) and multiplicative**. Eigenvalues of {{6af9626098a21e2d9b65d2f645788d82f71da73b71aff63bc3ec8ab956352bc9}} 
have nothing to do with eigenvalues of {{126c8331d32d16a65985d8df368f1905b208d48027ac66f59ac3c87762a28875}}.  

\[Lecture 22 starts here]

### Diagonalization

Suppose we have {{bb28a9b83048a0f36a72a56394914040f7f0171b49534f6138053bdd68916943}} linearly independent eigenvectors of {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}}, we put them in the columns of {{fdf30f5db1f3424874da244595a2db648c7b056dc537a2b62eb64b4d26d827ef}},

{{835f2674cfce539b7669911717c810ff04a6d44829c0c96126cca4aeb14d5a65}}

If {{fdf30f5db1f3424874da244595a2db648c7b056dc537a2b62eb64b4d26d827ef}} is invertible (if there are linearly indepenent, under our assumption), then we can write

{{ae6e65b63e429c04bd23784ab4ec9645e8bd8562297be62f25bb500a50f5d5f6}}


> ### Trace and determinant
> This part is only mentioned in the lectures but not deeply discussed, this part is meant to fill in that.  
>
> **Theorem.** The sum of all eigenvalues is equal the *trace* of {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}}, which is the sum of the main diagonal.  
> *Proof.* We take a look on the characteristic polynomal of matrix {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}}, we want to show that
> 
{{2d4f833c7326a7310899a7ae77bd226f0cc7c005441707dfdcdc990f9b44d2fb}}

> Consider {{c8f1d2b28dda134b8605934fc920b4fa923a2c2c168372731e1247bb703fbc00}}, for {{47b8239bac6ccbf39a8e6ec515697a0f4811ac63e52941ed4f418a8dd9675d82}}, the above equation holds.  
> Suppose all matrices with {{92d959d2fcb0c1e38936910d772695e8ca09769fddb08dfacc473553d9b18efa}} holds, for any matrix that is {{f7cd3aa406568d1c4ea308304b784465402e5403750014078db8ce6a59b99ff9}}, we have
> 
{{a4f533cd50df6e66e22ef2e6ee0e8d8afacfddb42ffb906b6764d8c0453280ec}}

> We want to keep the terms which have {{818d682922955bf09224dc505d046d271385d5e0c1ba9e2f592a1458910403ec}}. In the second matrix, the only way is to have {{6de94edcbd3ac08a3eb610004fe8323e7f75297ecee5aaa576b597248b07f18c}}. Because otherwise if we have {{19b1ba87796a5b4ffea5e15772323bb225a6be69fdb97bf567379ca7b03bf418}}, then for the rest {{2f837261f4d149c9d69138983e982cab2b2db12bd5225d31a7d164ae5241dbec}} of {{4042df424b41d18c79c774cff2736c4002b902ff2ce7e45779b31062f819d1cd}}s we can only choose maximum {{3f3eaeeb0fe9186c53924053f83ec5a6dec8777b2bf958b5cd59b1a999d639a5}} of them.  
> Therefore we are only interested in
> 
{{6c0349f381b83b054c53340a0fd692f2696918ece5b2a3b6f07030a2ac991b6e}}

> which is what we desired.  
> By math induction all finite square matrices have this property.  
>
> **Theorem.** The product of all eigenvalues is equal the *determinant* of {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}}.  
> *Proof.* Now we are interested in the last term of the charateristic polynomial:
> 
{{60cf90d68ccde5e2004d07fcae40027696b775dd22f235dbc07858d3315bfff9}}

> We can do the expand thing we have just done, but instead we drop all the terms having {{4042df424b41d18c79c774cff2736c4002b902ff2ce7e45779b31062f819d1cd}}, and we are left with {{380654258bbf25141939816740e339e071cfc778efeb4fc199ebcb40929cf6e5}}.  

### {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} powered
Suppose {{d333b06a487b87b0202af1b049b35a76987fd849ca1eef19391b0777c8847ac2}}, then for {{543112d5b99d7efa67e0a56d32cef5712479013bd3a26066bc1d6e47961aea51}},  

{{4fdbd58c17fce8ea1d9a9b0a987a85642920c3ffc81b6ae21db88a019c85214c}}

Same holds for the diagonalization we just have:

{{7376da6f34fb177e7bc4c6a8512edc3531a636804e2d594eb201be60f3534061}}


In fact we can do this *any integer times*, therefore

{{d16e98db6de901d670e32124af7b7f4ae8ebbfe288969c63d718b7e4fe186c98}}


{{0993965d8c921e6b499cee616cec7586f83c31c436edc72fa3ae953c98b4eda2}}


**Theorem.** {{236d46678318654c502444ba4bc06710680c2b5b608a51c1e65f2d8a24ad9703}} if all {{fea380737561909e9a6dbed2d6a115893b6d870d9fcf6d1b2a6dc47ee817b39d}}.  

When can we do such convenient thing? It turns out  
**Property.** {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} is sure to have {{bb28a9b83048a0f36a72a56394914040f7f0171b49534f6138053bdd68916943}} independent eigenvectors if all eigenvalues are different.  
> *Proof.*
> If we have only one vector {{fc926e2e053094d12274eaf384571f89d7737076907413559e8f11638b360c53}}, then {{fc926e2e053094d12274eaf384571f89d7737076907413559e8f11638b360c53}} is sure to be linearly independent.  
> Assume we already have {{82f5a56ad2b7c19620827b67a8c873175d166a2180c21c409090197b09afd62e}} linearly independent eigenvectors, then consider the {{2725b2d0fc640cb2728a1834f8c41d47e601a7313494a3c35628268f485f3a5f}}-th eigenvector.  
> We want to show that
> {{7406076db6221cd1552cff0584c8b2b554d7ccafb34fecd5751e9218aa48bf0d}} only have solution of {{939a370120a39ec6052d85cdc1777b702f42e8be948d8d936ed3941f85840020}}.  
> Let {{3954bad2e2115b523a34b161b61499ccfe8707700263067cd36e7d4c5a3e158b}}. The equation is equivlant to
> 
{{370eacbe14a43ad947f56edb69ad99a8e2804b691521bd814d50bf9705f0e03b}}

> Multiply both side by {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} gives
> 
{{60c1e6ad963a43995fec859ed085821e8091412611525138fcbc2f26fe120cbc}}

> Therefore if {{5568a4aa4ef3108c8947e1f3c6a7015eb309d3c080f9e4d6b253ae763b45f858}} is a solution, then {{80c9d212f7ae2505eb99efd5eaab5d87b027c2a376d81bb3a2c326e7452442a4}} is also a solution, which means  
> 
{{6c3a8b4635cd775b694d7f5e4ea7577a7d77b9fce9791be33fc24d5660e0ea7e}}

> Multiply the first equation by {{df1e59c67264b3e0289d0adbef6d6b88fb1a37ba2f96afcc4d08041bcac60fa1}} we get
> 
{{ad2dda261d5ac62e794862183b4f4b1f5ed5109bc67e9b01ae2bfb41543cb2f8}}

> If {{5568a4aa4ef3108c8947e1f3c6a7015eb309d3c080f9e4d6b253ae763b45f858}} is non-zero, then {{e58839c66329f0a78d5ab2beb7c539bf540ca077c2d455dbf833a4ef8838e4e5}} has at least two non-zero entries. Because all {{54ed025874a2dd317dfcb2073a4ee987a3e2f54508b1b433f3a4b5aca433e70a}} are different, at least one {{8f5b497f29f9a71c2cc5e9f2d450eef1f32f159bc2e00cf3701de1c6d403b14e}} is non-zero.  
> However by induction hypothesis, {{343663799d32e1d23a3885f3f561aa39ebba5b58b1c0b1ac95d82c38a0672ee3}} are linearly independent so {{167303ace7cee914991504c345fda65bac04dc9e3a05d4c179050b84857e81d9}} must be all zero.  
> We have met a contradiction and thus, there is no solution {{5568a4aa4ef3108c8947e1f3c6a7015eb309d3c080f9e4d6b253ae763b45f858}} other than zero and {{66b54ccf5c7187b8e71810f743806c8015736f59df78e5a9dd2b4899904f56e0}} are thus linearly independent.  
> By math induction, all eigenvectors are linear independent if their eigenvalues are different.   

#### Solving {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} powered
Suppose we have some column vector {{1a828f728dbe451e1ca047955ae6730bd7fa67ead62792398bb61efe898c6235}} and recursively {{a7bb87abf63746505b141023d247c0cc0b667e71a4835a1383c9dce401910101}}. How do we found {{9415bad4f7fcbf79918b16417462177995514dd117db15a3f2ace54bf9356354}}?  

Let's say {{c1ba8dcf3fa9c2a716c3819e37c3b466f812daa5cbb5815735cd8465ca095ae2}},  
then {{c05b787dfefdce95a7b967a6258f908237de3baba7c07b7a48fff757ed638626}}.  
Furthurmore, {{2057b93c83231cbd8034a1985e3cf2f1990d7cf93aea94f1dc08d17340c4b9e5}}.  
> In fact it is simply {{c42822964904f4b8bb6f932dc31266f1c278ffe16da0ef477cb7e6aa23bd54f5}}.  

For example we have Fibonacci sequence:

{{c9fad5f6cfdacc63c4d6952b9131602ace355e77daaa370a211e1b3063bfa07d}}

and we can build it as

{{dba0e00acf542043f4957435ebaf3d76468e0da7b44de8a5f7d4238865a51ed2}}

Solving it:

{{a28ca8eb0c559561e6c0da8217167b6470237d4f091636e2bb442e6e3214f206}}

Finding null space of {{ef43b6df43bfbeb21399d8799e89c0fc0de77785df6c30f6d1beabe304aee4e5}}:  
Since this matrix has a special property of {{e67ac591d38c69d55cdc97c2be96974daa96f7454439e339d6ccb099f96d91e0}},  

{{dbb2d5bfeee54b2d61df9faa1ef4c099ef30969fadf6f4d8934c41e8dba04c3d}}

and

{{6d7b3ecbc60e0c4e9e0d84f79e711e1ffff9e76c50d4a70bf7e8097d768320aa}}

We have

{{5988a177a56eea2a3a29739ce00c22bcc4826223b3d11e1eb8bc8c64bdb9b320}}


{{50ad7def85af0e92f9deda79c1221b901705469315b327cfca6c67ee654e24c4}}


\[Lecture 23 starts here]

### Differential Equations
In this part we are interested in systems look like this:

{{298e5c875d1cbe9b2a817ebaa69bf3a183b33927b0e6ac01ca77d8d1234968b2}}

Which can be write as

{{4248fabdba145336ef383e049c2c83db2d119f4959a80e17f360b8d0fd8c29ce}}

The special solution to this is

{{eed6d1d7326aea540906fb3f4e28aa84db018eadf7a6581724adb81e35e26f21}}

since

{{91fe0cadd882f3a76a2e58ddd453e72eb87681e8df5b5e5018c7b164565d86f2}}


Therefore we can solve these as

{{b0014805932e4128c61b6376aeac0b6f00202f7e1c7cb0652411cc4189f5ac94}}


Given some {{64caa526061b728c7364be9a40b7afd2e64e23e029a77282723c2a7832bc210f}}, we can do some elimination to obtain {{03aca84ea552160039fa508b227d5915b225a1c30124c7bdc37f98300ceb320e}}.  
There are some interesting property of *every* {{03aca84ea552160039fa508b227d5915b225a1c30124c7bdc37f98300ceb320e}}:
1. Stability. {{3928c0996de10ef21f6ec3a848fe3221aa535c2903e5a739f6b64e52f95a18f2}} if {{676983dbefd54a2910bd4cedb0d9191c8bd3e65eaa4a95d723dac8e3c69a90b3}}.  
   The imaginary part does not matter since {{83b5eaa01868860a8702abf210b539b896472338c816627edc0a57e1dd117f27}} and it always have the modular of {{72bc3c1b3553a71d525d8715f4963adfb2b8e7e18c32f0b1b651f3e841526770}}.  
2. Steady state. {{a2c6788bffbceff849093930882fbb0eba5549e8370daaadb87be3350cf0b189}} if some {{b0e2e3738cfd427783f387690f497610d7db0272fce2db439fc850068ac6529d}} and others have {{676983dbefd54a2910bd4cedb0d9191c8bd3e65eaa4a95d723dac8e3c69a90b3}}.  
3. Blow up. If any {{b45c79138de47261f83e0c3a86b4202516b1feef883a09d6dd9787a5f789fe00}}.  

Notes on {{b71be43b02045b8b4173d0bc2a348d09d5082ab0b79985e03def8bb55c796534}} variable differential equation: for matrix {{a69fb90e281b2859e4df5f598e3bd9e20baae1b6a6f4f68263310ecc751b6fbc}}, we can verify this matrix is stable or blowing up by {{d82469e3119b7b56cb119b4b3bc5f5bd930f4adcd81c4dbf507393d44a7a08c2}} and {{8eb6a6d9d7339b34df038f15ee9d7b47fc7829a0775b3c42852ca0263dbb6959}}.  

We can do more things than we current have.  
Let's say {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} has {{bb28a9b83048a0f36a72a56394914040f7f0171b49534f6138053bdd68916943}} independent eigenvectors, and for the vector function {{a924f6a91c6957d048bf210baea8dfe7727f90c8cd1a215285ee0fb22cfb169c}}, we find

{{8330473d14b2289f64f9ff6dc4611a42b6af9c7be72e374d66cf3ff037decd4b}}

then

{{c6276e5eac6925d89e1bb69ddb13910f937366f0b5057d4c266e66a6782072d6}}


{{a628f68dc96082811175704d40f7d2704eed104cf41f8872812e244323034a98}}

We are going to write that as

{{8dee53ffe1337b2a8a6df810643babdd6c4f44c2ccaa01f041d3dc7f80ec4888}}

Wait a minute, what is {{bb48247822852c86020a1de75b09d6a3b68963656342f17a01a3e7e9059c69bf}}? 

**Definition.** We define {{c420b80cf049595b293fc1bef738d2890c99c113eddc14ce70badbd211594a24}} by the Taylor Series:

{{87fd3cdbb708eab98de40bbf5f0f4fde7ec2c515ebaa14f4705d089b81e04aae}}


It is clear that

{{3475760536a0d0acfd5905d87c996ba1089290ec56a4505c0ef2590e4e93c9a9}}

if {{df91b9d8bde2bd79d3cb76137bd81f2206b660c9b7f45db5c393b3dc8b225e3e}} is diagonalizable.  

### Ordinary Differential Equation
Let's start with order {{b71be43b02045b8b4173d0bc2a348d09d5082ab0b79985e03def8bb55c796534}}:

{{484d383f521d7eb1789818ffe5f921c8d06d63c1c7c872aa6db5982f5c356f93}}

Setup a column vector by

{{ff690d7b800df9e4b9081ed89ecc0ffedbecbf764271f1dda6079768e6fade68}}

then

{{39a093884e729b06d57c06533e193bcdc02a3bc573f2709637ffefc56995d30d}}

and we have

{{69c27dca646cf914a71ad7c24698dd95f2cb5f41fb20a84eb68d41545183dc1a}}

which is solving 

{{71b09b8cd96788d7af1b079505c5e913feb8cc49d2a252021264a0b24ba74ceb}}


In fact, every ordinary differential equation with order {{bb28a9b83048a0f36a72a56394914040f7f0171b49534f6138053bdd68916943}} can be solved by setting


{{3c3e4d0b3aeb79819aaf956c6c40e0da5099773428cd0f9180129c4c88eeec00}}


and use the technique mentioned on previous section.  
