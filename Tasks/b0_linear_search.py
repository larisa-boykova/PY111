"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
	"""
	Function that find minimal element in array

	:param arr: Array containing numbers
	:return: index of first occurrence of minimal element in array
	"""
	min_el = arr[0]
	min_ind = 0
	for i in enumerate(arr):
		if i[1] < min_el:
			min_el = i[1]
			min_ind = i[0]

	print(arr)
	return min_ind
