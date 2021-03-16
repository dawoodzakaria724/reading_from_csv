
import csv


class SLDictionary:

    # function to read from a csv file
    @classmethod
    def dictionary_csv_file(cls, filename):
        with open('my_file.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)

            myList = []

            for line in csv_reader:
                myList.append(line)

            return myList


    @classmethod
    def dictionary_file(cls, filename):

        myList = []
        file1 = open(filename, 'r')

        for line in file1:
            x = line.split()
            x2 = int(x[0])
            myList.append([x2, x[1]])

        print(myList)

        file1.close()

        return myList

    @classmethod
    def save_dictionary(cls, filename):

        with open('my_file3.txt', 'w') as fileHandle:
            for listItem in filename:
                fileHandle.write('%s\n' % listItem)

    def __init__(self, arr):
        # sorts array, initializes dictionary, initializes _size
        arr.sort()
        self._dict_list = arr
        self._size = len(arr)
        self.head = None
        self.tail = None

    def __len__(self):
        # returns the size, so init must be completed
        return self._size

    def __contains__(self, key):

        return not self._find(key) is None

    def _find(self, key):  # _find reimplemented using binary search
        arr = self._dict_list
        low = 0
        high = len(self._dict_list) - 1
        mid = 0

        while low <= high:
            mid = (high + low) // 2
            if arr[mid][0] < key:
                low = mid + 1
            elif arr[mid][0] > key:
                high = mid - 1
            else:
                return " " + str(self._dict_list[mid][0]) + " " + str(self._dict_list[mid][1])

    # old version of _find

    """
          randStr = ""
          for x in self._dict_list:
            if x[0] == key:
              return randStr + " " + str(x[0]) + " " + str(x[1])
            else:
              return -1
    """

    def __getitem__(self, key):

        # calls _find, confirms if a certain key exists.

        index = self._find(key)

        if index is None:
            raise KeyError("Item does not exist in list")
        else:
            return index

    def __setitem__(self, key, value):
        self._insert(key, value)
        self._size += 1


    def _insert(self, key, value):

        testBool = False

        for x in self._dict_list:
            if x[0] == key:
                x[1] = value
                testBool = True
                break

        if not testBool:
            self._dict_list.append([key, value])
            self._dict_list.sort()


    def pop(self, key):
        for x in self._dict_list:
            if x[0] == key:
                # print("Popdebug")
                self._dict_list.remove(x)


    def __str__(self):  # print_dict
        testStr = ""
        for x in self._dict_list:
            # print(x)
            testStr = testStr + " " + str(x[0]) + " " + str(x[1])
        return testStr

    # old version of str, new version is print_dict

    # def __str__(self):

    # return str(self.key) + ": " + str(self.data)


    def _insertion_sort(arr):
        # Traverse through 1 to len(arr)
        for i in range(1, len(arr)):
            key = arr[i]
            value = arr[i][0]

            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i - 1
            while j >= 0 and key < arr[j][0]:
                arr[j + 1][0] = arr[j][0]

                j -= 1
            arr[j + 1] = key


    def partition(self, arr, low, high):
        i = (low - 1)  # index of smaller element
        pivot = arr[high]  # pivot

        for j in range(low, high):
            # If current element is smaller than or
            # equal to pivot
            if arr[j][0] <= pivot:
                # increment index of smaller element
                i = i + 1
                arr[i][0], arr[j][0] = arr[j][0], arr[i][0]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    # The main function that implements QuickSort
    # arr[] --> Array to be sorted,
    # low  --> Starting index,
    # high  --> Ending index
    # Function to do Quick sort


    def quickSort(self, arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.partition(arr, low, high)

            # Separately sort elements before
            # partition and after partition
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)


def main():

    # reading from a csv file and returning the data
    csvArr = SLDictionary.dictionary_csv_file("my_file.csv")
    print(csvArr)

    # array created from a file
    newArr = SLDictionary.dictionary_file("my_file.txt")

    arr = [[1, "John"], [3, "Jack"], [2, "Ann"]]

    dict = SLDictionary(arr)
    # testing to be sure the file version works
    newDict = SLDictionary(newArr)

    results = dict[1]

    # file version
    newResults = newDict[1]

    print(results)

    # file version
    print(newResults)

    print(dict)

    # file version
    print(newDict)

    dict[1] = "Test"

    # file version
    newDict[1] = "Test"

    results = dict[1]

    # file version
    newResults = newDict[1]

    print(results)

    # file version
    print(newResults)

    print(dict)

    # file version
    print(newDict)

    dict.pop(1)

    # file version
    newDict.pop(1)

    print(dict)

    # file version
    print(newDict)

    dict[7] = "Last"

    # file version
    newDict[7] = "Last"

    print(dict)

    # file verison
    print(newDict)

    SLDictionary.save_dictionary(newArr)


if __name__ == "__main__":
    main()
