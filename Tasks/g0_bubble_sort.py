from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with bubble sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	container = list(container)
	for i in range(len(container)):
		for i in range(len(container)-1):
			if container[i]>container[i+1]:
				container[i],container[i + 1]=container[i+1],container[i]


	return container
