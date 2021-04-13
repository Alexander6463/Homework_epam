from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    max_sum = 0
    for i in range(len(nums) - k + 1):
        sum = 0
        for j in range(i, i + k):
            sum += nums[j]
        if sum > max_sum:
            max_sum = sum
    return max_sum
