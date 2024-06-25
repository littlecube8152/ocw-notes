
## Miscellaneous Components

Multiplexer
Three-State Buffers -> Z: high impedance
Decoder
Encoder - priority scheme
ROM - read only memory

PLA - Programmable Logic Arrays

FPGA -> function generator
Shannon's Expansion: F(A, ...) = AF(1, ...) + A'F(0, ...), use substitution or K-map

## Latches & Flip-Flops

Latch: asynchronous
- SR Latch (Set-Reset)
  - 2 NAND or NOR
  - Switch debouncing
- Gated D Latch (Data)

Flip-Flop: synchronous -> setup time & hold time
- D Flip-Flop
  - 2 D Latch
- S-R Flip-Flop
  - S and R can only change when clock is high
- J-K Flip-Flop (00 Hold, 10 Jump, 01 Clear, 11 Toggle)
- T Flip-Flop (Toggle)

Additional inputs
- ClrN: clear (often inverted)
- PreN: set 1 (often inverted)
- CE: clock enable

## Registers
- Normal
  - D flip-flops, with clock and-ed with load
- Shift Register
  - Sequencial D flip-flops, shift if input is given
- PIPO Shift
  - Parallelly input, shift right if signal given
- Counter: using feedback 
  - K-map
  - Ensure don't care states falls to normal states, or reset upon power up

## State and Machines
 - Moore Machine: depending only on state
   - States: up: variable, down: output
 - Mealy Machine: state + input -> prone to glitches and spikes
   - Transitions: next input/output

Serial Data Transmission
 - NRZ, NRZI, RZ, Manchester

### State Reduction
($\lambda$ = output, $\delta$ = next state)

#### State Equivalence  
$p \in N_1 \equiv q \in N_2$ if and only if $λ_1(p, X) = λ_2(q,X)$, where $X$ is every possible input sequence 

#### Theorem
$p \in N_1 \equiv q \in N_2$ if and only if $λ_1(p, X) = λ_2(q,X)$ and $δ(p,X) \equiv δ(q,X)$ for all **single** input $X$.

#### Implication Table
- Draw a table (only half for simplification, full for equivlance test)
- Each square has at most two pairs
  - Putting condition that two state to be equivlant
  - For example A->B, C and D->E, F, put B-E and C-F
  - Cross out if output is already different
- Delete self implied pairs
- Keep on crossing out impossible pairs

#### State Assignment
Heuristic: Put "similar" states adjacent
 - same next state
 - same output
 - same (one of) previous state

One hot: speed

## Iterative circuit
