# 5 CPU Scheduling

Process consists of cycle of CPU and I/O burst.

- CPU scheduler: OS selects a process from ready queue to run
- Preemptive vs Non-preemptive (cooperative)
  - Non-preemptive only schedules when [running -> waiting] and [running -> terminate]
  - Preemptives also on [running -interrupt-> ready], [waiting -> ready]
- Dispatcher
  - dispatch a process  
  - switching context, switching mode, jumping

Aim: better use of CPU
- CPU utilization: busy
- Throughput: # of process
- Turnaround time: avg execution time
- Waiting time
- Response time: interactive (actually, minimize var is better)

## Scheduling Algo

- FCFS (First Come First Serve)
- SJF (Shortest Job First)
  - optimal
  - use exponential average to approximate
- RR (Round Robin)
  - everyone gets a time quantum
- Priority Scheduling
  - starvation -> aging
  - +RR
- Multilevel Queue 
  - priority scheduling, but a queue for each priority
  - inflexible
- Multilevel Feedback Queue 
  - multilevel queue, but process passing through them gets demoted
  - each queue can use different algo, for example 8 RR -> 16 RR -> FCFS

### Thread Scheduling
Modern OS use thread instead of process

Contention Scope
 - PCS (process contention scope) -> LWP, user lvl thread
 - SCS (system contention scope) -> kernel thread, scheduled by CPU scheduler
    - pthread lib supports both `PTHREAD_SCOPE_SYSTEM`

## Multi-Processor Scheduling
Multi-processor can be
 - Multi CPU
 - Multithread cores
 - Multicore CPU
 - NUMA
 - Heterogeneous MP


### Asymmetric vs Symmetric 
Asymmetric Multiprocessing
 - easy
 - master core becomes bottleneck
  
Symmetric Multiprocessing
 - Common queue vs Separate queue
   - often separate, locking becomes performance bottle neck

### Memory Stall
Cause by 
- CPU too fast, memory access too slow
- Cache miss

Can use up half of the time

Solution  
CMT (chip multithreading) - hardware threads (aka hyper-threading)
 - Coarse-Grained: switch on memory stall (or such long latency event)
   - overhead: unpredictable switch, requring flushin' pipeline
 - Fine-Grained: finer switching, often at boundary of instructions
   - predictable, can implement logic of doing so
  
Also a thread scheduling!
 - Ultra SPARC T3: RR
 - Intel Itanium: Priority

### Load Balancing
 - push migration vs pull migration

### Processor Affinity
 - caused by warm cache, NUMA arch
 - per-processor ready queues provide it for free!
 - soft affinity: only *prefer* to do so
 - hard affinity: required to do so

### Heterogeneous MP
 - big.LITTLE

## Real-Time CPU Scheduling

Characteristics
 - Periodic
 - Soft - only higher priority / Hard - deadlines

Event latency
 - Interrupt latency (interrupt arrival + context switch)
 - Dispatch latency 
   - confict phase - preemption and resource release
   - dispatch phase

Admission Control
 - Success or failure is determined upon submission

### Algorithms
 - Rate-Monotonic - smaller period higher priority
   - optimal for static priority algorithms
   - for a set of $n$ periodic tasks with unique periods, a feasible schedule that will always meet deadlines exists if the CPU utilization is below $n(\sqrt[n]2-1)$
 - EDF (earliest-deadline-first) 
 - Proportional Share
   - OS split time into $N$ shares, and a process get (possibly different) $T$ shares of them [https://dl.acm.org/doi/pdf/10.1145/321738.321743]

## OS Examples
### Linux
 - 2.5: O(1) scheduler
 - 2.6: CFS (completely fair scheduler)

nice value: -20 to +19
 - targeted latency: interval of time where each process should run at least once
 - virtual run time: using virtual clock to measure runtime
   - high-priority tasks run longer cuz clock ticks slower

Multiprocessor:
 - scheduling domain is a set of cores that can share load without much lose of efficiency
 - balancing starts with the lowest domain, and is reluctant to reschedule between NUMA nodes

### Windows
Called dispatcher

Priority:
 - variable class
 - real-time class

UMS (user-mode scheduling)

Multiprocessor
 - SMT sets: sets of logical processors
 - ideal processor
   - seeded, and increment across SMT sets

### Solaris 
Thread classes:
 - TS (time sharing)
 - IA (interactive)
 - RT (real time)
 - SYS (system)
 - FSS (fair share)
 - FP (fixed priority)

For each priority, there are
 - Time quantum
 - Time quantum expired: new priority for CPU-intensive thread
 - Return from sleep: new priority for short tasks

## Evaluation
 - Deterministic Modeling
   - take an example and run
 - Queueing Models
   - Thread CPU-burst and I/O-burst can be modeled
   - Little’s formula: $n$ (avg queue length) $=\lambda$ (avg arrival rate) $\times W$ (avg wait time)
 - Simulations
   - run
 - Implementation
   - test

# 11-15 IO and FS
## IO Devices
- HDD: Disk
  - **Sectors** -> **Tracks** -> **Cylinder**
  - Positioning time = Random-access time = Seek time + Rotational latency
  - Schedule: FCFS, SCAN, C-SCAN, deadline (FCFS + Batch), CFQ (wait for IO batch)
- NVM: SSD, USB
  - Durability: Drive Writes Per Day
  - Flash Translation Layer: map logical blocks to 
  physical page  
  - Slow to erase causes invalid block
    - Garbage Collection
    - Over-provisioning: keep an avaliable pool
    - Wear-leveling: keep writes averagely
    - Write amplification
  - Scheduling: NOOP (FCFS + adjacent heuristic)
- RAM drives
## Storage Attachment
- Each device has host controller (from computer) and device controller (in device) 
- Bus and daisy chain
  - A <-> B <-> C, bus has lanes (like road)
- Host-attached storage
  - ATA, SATA, SAS, USB, NMVe
  - FC (fibre channel) has HBA (host bus adapter) because its complex
  - SANs (RAID or JBOD)
- Network-attached storage
  - NFS, CIFS, iSCSI
  - RPC (Remote Procedure Call)
- Cloud storage
- 
## Logical Storage
- Block -> Clusters -> Device -> Partition -> Volume -> File System
- Special FS
  - Raw disk
  - Boot Block -> Boot Partition -> Boot Disk, which has MBR 
  - RAID
    - 0: strip, 1: mirror, 4: parity disk, 5: distributed 4, 6: PQ redundancy
  - ZFS
    - Like RAID, but managed on block level (pool of partitions)
  - Object storage 
    - Hadoop, Ceph
    - horizontal scalability, content-addressable storage
- Snapshot
- Reiplication: Copy on write

## IO
### Hardware methods
- Polling
  - Ping device like spin lock
- Interrupts
- Memory-Mapped I/O
  - Efficient (lazy read and page algo)
- Direct Memory Access
  - More efficient (no CPU work is done except for 2 interrupts)
  - Scatter-gather allow multiple transfer (batch)

### Software calls
- Block-device Interface
  - disk, read write
- Character-stream interface
  - keyboard, get put
- Timer
  - actually just interrupt
- Nonblocking IO
  - multithreading
- Asynchronous IO
  - signal, interrupt, call-back
- Vectored IO
  - vectorized!

### Hierachy
Program -> Logical FS -> File organization module -> Basic FS -> IO control -> Device
- File organization module understands files, logical address, and physical blocks
- Basic FS does block IO

### Kernel subsystem
- Scheduling
  - device-status table
- Buffering
  - double buffering
  - copy semantics
- Caching
  - buffer cache + page cache -> unified vm
  - free behind + read ahead
- Spooling
  - some device (e.g. printer) cannot multiplex, should queue
- Error Detection
  - additional sense code
- I/O Protection
- Power management
  - ACPI

## FS
### General Terms
- Volume Control Block (master file table, superblock)
- File Control Block (inode)
- mount table
- system-wide/per-process open file table

## Directory Structure
- Single-Level Directory: all in root
- Two-Level Directory: all in home
- Tree-Structured Directories
- Acyclic-Graph Directories
- General Graph Directory
  - cycle referencing
  - garbage collection: traversing the entire file system, and remove unaccessable file

### Allocation
- Contiguous allocation
  - External fragmentation
  - File can grow -> adding extent -> Internal fragmentation
- Linked allocation
  - One pointer break = file lost
  - Slow search
  - Varation: FAT (store linked table separately)
- Indexed allocation
  - save at index block
  - direct, single indirect, double indirect, triple

### Free-Space Management
- Bit vector
  - MP4
- Linked List
  - Grouping (group id into block like FAT)
  - Counting (compress continguous)

### Recovery
- Consistency Checking
- Log-Structured File Systems
  - operation (transaction) are logged
  - aborted transaction: undo then all redo
- Snapshot: keep new copy on change
- Clone: read only snapshot (copy-on-write)
- State information (for remote storage)
  - used to recover when server fails or connection fails

### VFS
unified interface for managing multiple filesystems

# 6-7 Synchornization
Main problem: race condition
No such issue in nonpreemptive kernels
## Formulation: Critical-Section 
entry - critical - exit - remainder
should satisfy
 - Mutual exclusion
 - Progress
 - Bounded waiting
### Peterson’s Solution
```cpp
int turn;
bool flag[2];
while (true) {
  flag[i] = true;
  turn = j;
  while (flag[j] && turn == j);
  /* critical section */
  flag[i] = false;
  /*remainder section */
}
```
If both process wants to enter, only one will enter, and it will set turn the the other process.

Issue: modern computer change not dependent instruction to improve efficiency
Solution: 
- Memory Barriers
  - all loads and stores are completed: a boundary of instruction
- Atomic instruction
  - test_and_set
  - compare_and_swap
    - if value is expected, modify to newval and return original
- Atomic variables

## Tools
### Mutex Locks
 - Disadvantage: busy waiting
### Semaphores
 - wait -> sleep
 - signal -> wakeup
### Monitors
 - Like an interface
 - Intuition: one bad usage can crash the whole party
 - Abstract Data Type
   - Condition Variable: `wait`, `signal`
   - Signal and wait: signaler wait until the other completes
   - Signal and continue: signaler finishes and the other resume
 - One function can be run at the same time

For example, we have comsumer and producer. 
Consumer has nothing to do until there are something in the buffer.
Let `x` be the variable associated with non-empty buffer, then producer will `x.signal` and consumer will `x.wait`.
We use `next` for suspension.

any function:
```
wait(mutex)
...
if (next_count > 0) signal(next);
else                signal(mutex);
```

x.wait:
```
x_count++;
if (next_count > 0) signal(next);
else                signal(mutex);
wait(x_sem);
x_count--;
```

x.signal:
```
if (x_count > 0) {
  next_count++;
  signal(x_sem);
  wait(next);
  next_count--;
}
```
### Transactional Memory
Use atomic block
### Functional Programming Languages
Non mutable -> no lock

## Issues
### Deadlock

### Priority Inversion
Higher priority process is blocked by lower priority, and a medium priority cut in. High priority is thereby fake.

Solutoin: priority of a process is the max of pri of process which needs the same resource as it

## Bounded-Buffer Problem
## Reader-Writer Problem
- First: Writer might starve.  
Writer: obtain `rw_mutex`.  
Reader: use `mutex` as a queue. Queue top is like a "leader", which waits `rw_mutex`. Then, when it is scheduled, all current process in `mutex` is signaled and read concurrently. Then, everyone wait until the read is done, and everyone leaves and signals `rw_mutex`.
## Dining-Philosophers Problem





2, 4, 1, 0, 1
AABBC CDDEE AABBC CEEAA BBCEB B
A 20
B 26
C 23
D 8
E 24