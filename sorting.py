class Sorting:

    def __init__(self):
        pass

    def insertion_sort(self, array):
        for i in range(1, len(array)):
            shift = array[i]
            j = i - 1

            while j >= 0 and shift < array[j]:
                array[j + 1] = array[j]
                j -= 1
                array[j + 1] = shift
        return self.show_array(array)
    
    @staticmethod
    def show_array(array):
        """
        Prints an array
        :rtype: object
        """
        for i in range(len(array)):
            print("% d" % array[i])
