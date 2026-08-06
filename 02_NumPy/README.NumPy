# NumPy Learning Portfolio (Days 1–4)

Hands-on NumPy practice — array fundamentals, vectorized operations, and two mini-projects — as part of my Data Science/ML learning sprint.

## Structure

| File | Topic |
|---|---|
| [Day1_NumPy_Basics.py](./Day1_NumPy_Basics.py) | Array creation, indexing, reshaping |
| [Day2_NumPy_Operations.py](./Day2_NumPy_Operations.py) | Vectorized ops, broadcasting, aggregation |
| [Day3_Student_Marks_Analysis.py](./Day3_Student_Marks_Analysis.py) | Mini-project: marks dataset analysis |
| [Day4_NumPy_vs_Python_Lists_Benchmark.py](./Day4_NumPy_vs_Python_Lists_Benchmark.py) | Mini-project: performance benchmarking |

## Day 1 — Fundamentals
- Array creation: `arange()`, `zeros()`, `ones()`, `linspace()`, random generation
- 1D/2D arrays, shape/size/ndim/dtype
- Indexing, slicing, reshaping

## Day 2 — Operations & Analysis
- Element-wise math (square, sqrt, median), array-array ops
- Boolean masking, filtering, broadcasting
- Aggregations: sum, mean, max, min, variance, std
- Axis-wise operations on 2D arrays

## Day 3 — Mini Project: Student Marks Analysis
Analyzes a student marks dataset using NumPy:
- Per-student total and average marks
- Per-subject highest/lowest/average
- Automatic grade assignment based on performance

Applies 2D arrays, axis operations, aggregation, and conditional logic on structured data.

## Day 4 — Mini Project: NumPy vs Python Lists Benchmark
Benchmarks NumPy arrays against native Python lists for addition, multiplication, square root, sum, mean, and memory usage, using `time.perf_counter()`, `math`, and `sys`.

**Findings:** NumPy consistently outperformed Python lists on execution speed and memory efficiency, with the gap widening as dataset size increased.

## Tech Stack
Python 3 · NumPy · `time` · `math` · `sys`

## Next Step
Moving to **Pandas** — real-world dataset cleaning, transformation, and exploratory data analysis.