class Searching:

    def binary_search(self, array, left, right, item):
        """
        An implementation of the binary search
        algorithm
        :param array:
        :param left:
        :param right:
        :param item:
        :return:
        """
        if right >= left:
            mid = left + (right - 1) // 2

            if array[mid] == item:
                return mid
            elif array[mid] > item:
                return self.binary_search(array, left, mid - 1, item)
            else:
                return self.binary_search(array, mid + 1, right, item)
        else:
            return -1

    @staticmethod
    def display_result(result):
        """
        Displays the result of the binary search
        :param result:
        :return:
        """
        if result == - 1:
            print("***********")
            print("Element is not present in array")
        else:
            print("***********")
            print("Element is present at index % d" % result)
