# Needleman-Wunsch Global Sequence Alignment

## 1. Introduction
The **Needleman-Wunsch Algorithm** is an optimal global sequence alignment algorithm based on dynamic programming. First proposed in 1970 by Saul B. Needleman and Christian D. Wunsch, it is widely used in bioinformatics to compare nucleotide (DNA/RNA) and amino acid (protein) sequences end-to-end, as well as in natural language processing and text diffing.

Global alignment is most appropriate when aligning two sequences of roughly similar lengths that are expected to share homology or similarity across their entire spans.

## 2. Usage


from NeedlemanWunsch import NeedlemanWunsch

# Instantiate aligner with custom scoring parameters
aligner = NeedlemanWunsch(match_score=2, mismatch_penalty=-1, gap_penalty=-1)

# Define sequences
seq1 = "GATTACA"
seq2 = "GCATGCT"

# Perform global alignment
score, aligned1, aligned2 = aligner.align(seq1, seq2)

print(f"Optimal Score: {score}")
print(f"Aligned Seq 1: {aligned1}")
print(f"Aligned Seq 2: {aligned2}")

# Retrieve DP Matrix
dp_matrix = aligner.get_score_matrix(seq1, seq2)


## 3. Detailed Explanation
The algorithm operates in three main stages:

1. **Initialization:** A grid/matrix of dimensions `(m + 1) x (n + 1)` is allocated, where `m` and `n` are the lengths of `seq1` and `seq2` respectively. The first row and column are populated by accumulating the `gap_penalty` values representing consecutive gaps.
2. **Matrix Filling (Dynamic Programming):** For each cell `(i, j)`, the score is calculated from three neighboring predecessor cells:
   - **Diagonal (`i-1`, `j-1`):** Represents aligning character `seq1[i-1]` with `seq2[j-1]` (rewarded with `match_score` or penalized with `mismatch_penalty`).
   - **Up (`i-1`, `j`):** Represents aligning `seq1[i-1]` to a gap `'-'` in `seq2` (penalized with `gap_penalty`).
   - **Left (`i`, `j-1`):** Represents aligning a gap `'-'` in `seq1` to `seq2[j-1]` (penalized with `gap_penalty`).
   The cell takes the maximum of these three options: `DP[i][j] = max(Diagonal, Up, Left)`.
3. **Traceback:** Starting from cell `(m, n)`, the algorithm steps backwards toward `(0, 0)` following the choice that produced the optimal score, reconstructing the aligned strings with gaps inserted where vertical or horizontal transitions occurred.

## 4. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(m \times n)$ where $m$ and $n$ are the lengths of `seq1` and `seq2`. Every cell in the $(m+1) \times (n+1)$ matrix is computed in $\mathcal{O}(1)$ time, and traceback takes $\mathcal{O}(m + n)$ steps.
- **Space Complexity:** $\mathcal{O}(m \times n)$ to store the $(m+1) \times (n+1)$ dynamic programming scoring table and traceback matrix.
