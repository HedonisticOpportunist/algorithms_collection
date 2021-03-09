from sorting import Sorting
from searching import Searching

ARRAY_TO_SORT = [12, 11, 13, 5, 6]
ARRAY_TO_SEARCH = [2, 3, 4, 10, 40]
ITEM = 1

sorting = Sorting()
sorting.insertion_sort(ARRAY_TO_SORT)
sorting.bubble_sort(ARRAY_TO_SORT)

searching = Searching()
result = searching.binary_search(ARRAY_TO_SEARCH, 0, len(ARRAY_TO_SEARCH) - 1, ITEM)
searching.display_result(result)

