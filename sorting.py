class Sorting:

    def __init__(self):
        pass

    def insertion_sort(self, array):
        """
        An implementation of the insertion sort
        algorithm
        :param array:
        :return: the sorted array
        """
        for i in range(1, len(array)):
            shift = array[i]
            j = i - 1

            while j >= 0 and shift < array[j]:
                array[j + 1] = array[j]
                j -= 1
                array[j + 1] = shift
        return self.show_array(array)

    def bubble_sort(self, array):
        """
        An implementation of the bubble sort
        algorithm
        :param array:
        :return: the sorted array
        """
        for i in range(len(array)):
            for j in range(0, len(array) - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]

            return self.show_array(array)

    def quick_sort(self, array, low, high):
        """
        An implementation of the quick sort
        algorithm
        :param array:
        :param low:
        :param high:
        :return: the sorted array
        """
        if low < high:
            partition_index = self.partition(array, low, high)
            self.quick_sort(array, low, partition_index - 1)
            self.quick_sort(array, partition_index + 1, high)
        return self.show_array(array)

    def merge_sort(self, array):
        """
        An implementation of the merge sort
        algorithm
        :param array:
        :return: the sorted array
        """
        if len(array) > 1:
            mid = len(array) // 2

            left = array[:mid]
            right = array[mid:]

            self.merge_sort(left)
            self.merge_sort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1
            return self.show_array(array)

    @staticmethod
    def show_array(array):
        """
        Prints an array
        :rtype: object
        """
        for i in range(len(array)):
            print("% d" % array[i])
        print("--(.=^・ェ・^=)--")

    @staticmethod
    def partition(array, low, high):
        """
        Partitions an array
        :param array:
        :param low:
        :param high:
        :return:
        """
        i = (low - 1)
        pivot = array[high]

        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]

        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1
