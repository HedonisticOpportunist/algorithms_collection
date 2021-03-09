from sorting import Sorting
from searching import Searching

ARRAY_TO_SORT = [12, 11, 13, 5, 6]
ARRAY_TO_SEARCH = [2, 3, 4, 10, 40]
OTHER_ARRAY_TO_SEARCH = [4, 2, 6, 9, 2]
ITEM = 1

sorting = Sorting()
sorting.insertion_sort(ARRAY_TO_SORT)
sorting.bubble_sort(ARRAY_TO_SORT)
length = len(OTHER_ARRAY_TO_SEARCH)
sorting.quick_sort(OTHER_ARRAY_TO_SEARCH, 0, length - 1)
sorting.merge_sort(OTHER_ARRAY_TO_SEARCH)

searching = Searching()
result = searching.binary_search(ARRAY_TO_SEARCH, 0, len(ARRAY_TO_SEARCH) - 1, ITEM)
searching.display_result(result)
