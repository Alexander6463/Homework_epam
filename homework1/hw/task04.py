from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
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
