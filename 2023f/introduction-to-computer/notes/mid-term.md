
## Numbers
1 Bytes = 2 Nibbles = 8 Bits  
#### Sign/Magnitude Numbers
 - <span style="color: #FF8888">1 bit sign</span> + <span style="color: #88CCFF">N - 1 bits number</span>: $(-1)^{a_{N-1}} \sum_{i=0}^{N-2} 2^ia_i$
 - Range: $(-2^{N-1}, 2^{N-1})$
 - Difficult to add two numbers
#### Two’s Complement Numbers
 - <span style="color: #FF8888">1 bit sign</span> + <span style="color: #88CCFF">N - 1 bits number</span>: $-2^{N-1}{a_{N-1}} + \sum_{i=0}^{N-2} 2^ia_i$
 - $\textbf 0$ = <span style="color: #FF8888">0</span><span style="color: #88CCFF">000...0</span>, $\textbf{-1}$ = <span style="color: #FF8888">1</span><span style="color: #88CCFF">111...1</span>, $\textbf2^{N-1}\textbf{-1}$ = <span style="color: #FF8888">0</span><span style="color: #88CCFF">111...1</span>, $\textbf{-2}^{N-1}$ = <span style="color: #FF8888">1</span><span style="color: #88CCFF">000...0</span>
 - Range: $[-2^{N-1}, 2^{N-1})$
 - $-x = \char`~x + 1$
 - Extension: Pad $a_{N-1}$.

## Logic Gates and Circuits

AND, OR, XOR

### Combinational Circuit
- Combinational
- No loop

Complement: Negation of a variable  
Implicant: Product of a variable  
Minterm: (Sum of) Products $= \sum(\cdot)$  
Maxterm: (Product) of Sums $= \prod(\cdot)$  

### Circuit Schematics Rules
Inputs on the top, Output on the right, Gates flow from left to right.

### K-Maps

### State Diagram / Automaton


