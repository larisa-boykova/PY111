from typing import Any, Sequence, Optional


def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	ind_start = 0
	ind_stop = len(arr)

	while True:
		if ind_start==ind_stop:
			return None
		mid_ind = int((ind_stop - ind_start) / 2)+ind_start
		if elem == arr[mid_ind]:
			return mid_ind

		if elem < arr[mid_ind]:
			ind_stop = mid_ind

		if elem > arr[mid_ind]:
			ind_start = mid_ind + 1

