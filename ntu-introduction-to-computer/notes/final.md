## Introduction to Computers (2023 Fall 01) Final Notes
## Digital Circuits
### Adders
#### Half Adder
Input: $A, B$.  
Output: $A + B = 2C_{out} + S$.  
#### Full Adder
- Input: $A, B, C_{in}$.  
- Output: $A + B + C_{in} = 2C_{out} + S$.  
#### Ripple-carry Adder
Pipe each adder's $C_{out}$ to the next adder's $C_{in}$. Very slow.  
#### Carry-lookahead
- Idea: Split adders into chunks (blocks) and precompute possible carries.  
- Key observation: Let $p_i, g_i$ be **propagate** and **generate** carry. We can expand all carries using lots of basic circuit: $P_{k:0} = p_kP_{k-1:0}, G_{k:0} = g_k + p_kG_{k-1:0}$
- Although it takes much space and basic circuit, sequencially adding numbers are still too slow. Therefore carry-lookahead is a much faster approach.
- Time: $t_{pg} + t_{PG} + (N/k – 1)t_{AND/OR} + kt_{FA}$
#### Prefix adder
- Not covered in class.
- Idea: Treat $P, G$ as prefix sum problem.
- Estimated time: $t_{pg} + \log_2N \cdot t_{PG} + t_{XOR}$

### ALU
Input: 2 N-bit integers $A, B$ (called **operands**) and a code $F$ indicating what calculation to perform.

Output:
| $F_{2:0}$ | Function |
| -:        | :-:      |
| 000       | A & B    |
| 001       | A \| B   |
| 010       | A + B    |
| 011       | not used |
| 100       | A & ~B   |
| 101       | A \| ~B  |
| 110       | A - B    |
| 111       | A < B    |

How does that work?

1. $F_2$ selects whether `B` should be inverted.
2. If $F_{1:0}$ is `0` or `1`, the multiplexer selects "AND"-ed or "OR"-ed result.
03. Otherwise, `A` is added with `B` if $F_2$ is `0` and `~B + 1` = `-B` otherwise.
4. If the $F_{1:0}$ is `2`, output the result. Otherwise output the MSB with zero extended.

### Rotate and shifter
#### Notation
Left is MSB, right is LSB.
- Logical shifter: shift and pad with `0`.
- Arithmetic shifter: shift and pad with MSB.
- Rotator: rotate.

### Counters
- Just what you are thinking. An adder and a D flipflop.

### Shift Registers
- Shift a bit out and a bit in on clock edge.
- LFSR

### Memory Arrays

- SRAM (Static RAM) -> Cache Memory
  - Fastest
  - Takes power only on write
  - Expensive and complex
- DRAM (Dynamic RAM) -> RAM
  - Fast
  - Takes power
- ROM -> Disk
  - Slow for writing (or even not possible, for example flash memory)
  - Does not lose data when power off

## Floating Point Numbers
- Write any real number as **binary scientific notation**: $\pm M \times 2^{E}$.
- Sign bit: $\pm$. 
- Exponent bits: **biased**, it is `0x011...111` + $E$.
- Mantissa bits: since $M$ has 1 in most situation, only numbers after decimal point is stored. Default rounding mode is **round-to-nearest (even number if same)**.

For 32 bits, it is 1-8-23 (bias 127), and for 64 bits, it is 1-11-53 (bias 1023).

- Special Numbers  

| Special Numbers | Sign | Exponent | Mantissa |
| :-              |  -   | -:       | -:       |
| $\pm 0$ | $\pm$ | `0` | `0` |
| $\pm \infty$ | $\pm$ | `111...1` | `0` |
| `NaN` | X | `111...1` | non-zero

## Python
Easily forgotten tricks

- `list.extend(list)` extend a list to a list
- `dict.keys()`, `dict.values()`, `dict.items()`
- `dict.update(dict)` or `dict |= dict`: merge two `dict`s
- `set.add(key)`
- `enumerate(iterable)`: make each element as a tuple with id (0-indexed) at the begin  
  ```py
  l = ["little", "cube", "is", "dumb"]
  for idx, s in enumerate(l):
    print(idx, s)
  ```
- `zip(iterable, iterable)` weird and idk how to explain
    ```py
    l1 = [1, 2, 3]
    l2 = ['a', 'b', 'c', 'd']
    for i, j in zip(l1, l2):
        print(i, j)
    # 1 a
    # 2 b
    # 3 c
    d1 = {"a": 1, "b": 2, "c": 3}
    d2 = {"a": 1, "b": 4, "d": 5}
    for a, b in zip(d1, d2):
        print(a, b)
    # a a
    # b b
    # c d
    for a, b in zip(d1.items(), d2.items()):
        print(a, b)
    # ('a', 1) ('a', 1)
    # ('b', 2) ('b', 4)
    # ('c', 3) ('d', 5)
    ```
- function in class: always remember `self` or `@classmethod` + `cls`!
- file object: can iterate though lines by `f` or `f.readlines()`
- `map(func, iterable)`: apply `func` to all items in `iterable`, most likely used by `list(map(...))` combo.
- `filter(func, iterable)`: preserve if `func` return `True`.

## Git
Nothing important. It is your daily life.

## Computer Artitechture
### CISC vs. RISC
| CISC | RISC |
|  --  |  --  |
| Hardware | Software |
| Complex and large instruction set | Few instructions |
| Less registers | More registers |
| Microprogramming | Compleity in Computer |
| Difficult Pipeline | Easy Pipeline |

## Assembly and Hack Computers

### A instruction
`@value`: `0vvv vvvv vvvv vvvv`
Set the register A's value to `value`. Increase pc by 1.

### C instruction
`dest=comp;jump`: `111a cccc ccdd djjj`  
Set all registers in `dest` to the result of `comp`, and jump according to condition specified by `jump` (store A to pc). If no jump is performed, pc is increased by 1.

### Word, Bytes, Big- and Small-Endian
LW, LB, SW, SB all use **bytes** as offset. A word is usually 32 bits and a byte is 8 bits.

Assume the data is 0x23456789.

- Big endian: MSB stores first.
  
|Value|23|45|67|89|
|-|:-:|:-:|:-:|:-:|
|Address|0|1|2|3|

- Small endian: the reverse

|Value|89|67|45|23|
|-|:-:|:-:|:-:|:-:|
|Address|0|1|2|3|

It can be think as, **the order within each byte is always big-endian!** However, that is not true. It is just because all of small endian is reversed, so it is interpreted like that (if you apply offset by bits, you have to actually reverse all bits, though there might be no assembly language does that).

## Databases


Degree and Cardinality
• Degree is the number of fields in schema
• Cardinality is the number of tuples in relation

- `CREATE TABLE tablename (columnname type, ... [UNIQUE, PRIMARY KEY, FOREIGN KEY, CHECK])`
  - `type`: `integer`, `real`, `char(length)`
  - \*All of the following can add a `CONSTRAINT constraintname` as a prefix.
  - `UNIQUE (columnname, ...)` force these columns to be unique
  - `PRIMARY KEY (columnname)`
  - `FOREIGN KEY (columnname) REFERENCES tablename [ON ...]`
    - `ON ...` can be one of `ON DELETE`, `ON UPDATE`, and it should follow with one of `CASCADE` (remove), `NO ACTION`, `SET DEFAULT` or `SET NULL`.
  - `CHECK constraint`
- `DROP TABLE tablename`
- `ALTER TABLE tablename ADD columnname type`
- `ALTER TABLE tablename DROP columnname`
- `INSERT INTO tablename [columns] VALUES (...)`
  - `columns` are optional
- `DELETE FROM tablename [WHERE ...]`
- `UPDATE tablename SET ... [WHERE ...]`
- `SELECT [DISTINCT] columns FROM table [WHERE ...]`
  - If multiple tables were selected, it uses set Cartesian (cross) product.
  - `LIKE`: `_` represent a character, `%` represent any number of characters (similar to `.` and `.*` in regex)
  - `IN`: just as what you think.
  - `EXISTS`: keep if the query is not empty.
  - `UNIQUE`: keep if the query does not contain duplicates.
  - `key comparator ANY/ALL (subquery)`: `ANY` means at least one, `ALL` means all.
- `UNION [ALL]`, `INTERSECT [ALL]`, `EXCEPT [ALL]`: between two `SELECT` queries. Use `ALL` to retain duplicates.
- Aggregate operators: `COUNT([DISTINCT])`, `SUM`, `AVG`, `MAX`, `MIN`.
  - Can use `COUNT(CASE WHEN condition THEN 1 ELSE NULL END)`!
  - Often used with `GROUP BY`
- `HAVING`: affected by group by
- `CREATE ASSERTION assertionname CHECK (...)`
  - Not associated with any table, exists globally.
- `CREATE TRIGGER triggername AFTER event [WHEN condition] action`
