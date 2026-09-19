from typing import Tuple, List, Optional


class NeedlemanWunsch:
    """
    A production-grade implementation of the Needleman-Wunsch algorithm
    for global sequence alignment using dynamic programming.
    """

    def __init__(
        self,
        match_score: int = 1,
        mismatch_penalty: int = -1,
        gap_penalty: int = -1
    ) -> None:
        """
        Initializes the Needleman-Wunsch aligner with custom scoring parameters.

        :param match_score: Reward score for matching characters (typically positive).
        :param mismatch_penalty: Penalty score for mismatched characters (typically negative or zero).
        :param gap_penalty: Penalty score for inserting a gap (typically negative).
        """
        if not isinstance(match_score, int):
            raise TypeError("match_score must be an integer.")
        if not isinstance(mismatch_penalty, int):
            raise TypeError("mismatch_penalty must be an integer.")
        if not isinstance(gap_penalty, int):
            raise TypeError("gap_penalty must be an integer.")

        self.match_score: int = match_score
        self.mismatch_penalty: int = mismatch_penalty
        self.gap_penalty: int = gap_penalty

    def _compute_matrices(
        self, seq1: str, seq2: str
    ) -> Tuple[List[List[int]], List[List[str]]]:
        """
        Helper method to compute the DP score matrix and traceback pointers.

        :param seq1: First sequence.
        :param seq2: Second sequence.
        :return: A tuple of (score_matrix, traceback_matrix).
        """
        m, n = len(seq1), len(seq2)

        # Initialize DP and Traceback matrices
        score_matrix: List[List[int]] = [[0] * (n + 1) for _ in range(m + 1)]
        traceback_matrix: List[List[str]] = [[""] * (n + 1) for _ in range(m + 1)]

        # Initialize base cases (first row and first column)
        for i in range(1, m + 1):
            score_matrix[i][0] = score_matrix[i - 1][0] + self.gap_penalty
            traceback_matrix[i][0] = "U"  # Up (Gap in seq2)

        for j in range(1, n + 1):
            score_matrix[0][j] = score_matrix[0][j - 1] + self.gap_penalty
            traceback_matrix[0][j] = "L"  # Left (Gap in seq1)

        traceback_matrix[0][0] = "DONE"

        # Populate DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                char1 = seq1[i - 1]
                char2 = seq2[j - 1]

                match_or_mismatch = (
                    self.match_score if char1 == char2 else self.mismatch_penalty
                )
                diag_score = score_matrix[i - 1][j - 1] + match_or_mismatch
                up_score = score_matrix[i - 1][j] + self.gap_penalty
                left_score = score_matrix[i][j - 1] + self.gap_penalty

                max_score = max(diag_score, up_score, left_score)
                score_matrix[i][j] = max_score

                # Standard preference order for traceback: Diagonal > Up > Left
                if max_score == diag_score:
                    traceback_matrix[i][j] = "D"
                elif max_score == up_score:
                    traceback_matrix[i][j] = "U"
                else:
                    traceback_matrix[i][j] = "L"

        return score_matrix, traceback_matrix

    def align(self, seq1: str, seq2: str) -> Tuple[int, str, str]:
        """
        Performs global sequence alignment on seq1 and seq2.

        :param seq1: The first sequence string (e.g., DNA/RNA/protein or text).
        :param seq2: The second sequence string.
        :return: A tuple containing (optimal_alignment_score, aligned_seq1, aligned_seq2).
        :raises TypeError: If seq1 or seq2 are not strings.
        """
        if not isinstance(seq1, str) or not isinstance(seq2, str):
            raise TypeError("Both sequences must be strings.")

        m, n = len(seq1), len(seq2)
        score_matrix, traceback_matrix = self._compute_matrices(seq1, seq2)
        optimal_score = score_matrix[m][n]

        # Traceback phase
        aligned_seq1: List[str] = []
        aligned_seq2: List[str] = []
        curr_i, curr_j = m, n

        while curr_i > 0 or curr_j > 0:
            direction = traceback_matrix[curr_i][curr_j]
            if direction == "D":
                aligned_seq1.append(seq1[curr_i - 1])
                aligned_seq2.append(seq2[curr_j - 1])
                curr_i -= 1
                curr_j -= 1
            elif direction == "U":
                aligned_seq1.append(seq1[curr_i - 1])
                aligned_seq2.append("-")
                curr_i -= 1
            elif direction == "L":
                aligned_seq1.append("-")
                aligned_seq2.append(seq2[curr_j - 1])
                curr_j -= 1
            else:
                break

        aligned_str1 = "".join(reversed(aligned_seq1))
        aligned_str2 = "".join(reversed(aligned_seq2))

        return optimal_score, aligned_str1, aligned_str2

    def get_score_matrix(self, seq1: str, seq2: str) -> List[List[int]]:
        """
        Returns the filled dynamic programming score matrix for two sequences.

        :param seq1: The first sequence string.
        :param seq2: The second sequence string.
        :return: A 2D list representing the (m+1) x (n+1) scoring matrix.
        :raises TypeError: If seq1 or seq2 are not strings.
        """
        if not isinstance(seq1, str) or not isinstance(seq2, str):
            raise TypeError("Both sequences must be strings.")

        score_matrix, _ = self._compute_matrices(seq1, seq2)
        return score_matrix
