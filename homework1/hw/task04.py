"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
compute how many tuples (i, j, k, l) there are such
that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int],
                      c: List[int], d: List[int]) -> int:
    count = 0
    dct_sum = {}
    for element_a in a:
        for element_b in b:
            if element_a + element_b not in dct_sum:
                dct_sum[element_a + element_b] = 1
            else:
                dct_sum[element_a + element_b] += 1
    for element_c in c:
        for element_d in d:
            if -1 * (element_c + element_d) in dct_sum:
                count += dct_sum[-1 * (element_c + element_d)]
    return count
