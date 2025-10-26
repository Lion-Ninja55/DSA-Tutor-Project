def ArraysLesson():
    print("\nThis lesson is under construction.\n")

def MinValFind():
    print("\nMinimum Value Detector\n")

    nums_list = []
    items = int(input("How many numbers would you like in your list? "))
    print(f"\nYou will be asked to enter {items} numbers for your list. No duplicates allowed.\n")

    while len(nums_list) < items:
        try:
            num = float(input(f"Enter a number {len(nums_list)+1}: "))
            if num in nums_list:
                print("Duplicate detected. Try a different number.\n")
            else:
                nums_list.append(num)
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    min_num = min(nums_list)
    print(f"\nThe lowest value in your list is {min_num}\n")

def BinarySearcher():
    import random
    print("\nBinary Searcher\n")

    def binarySearch(arr, targetVal):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == targetVal:
                return mid
            elif arr[mid] < targetVal:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    try:
        mylist = []
        vals = int(input("How many numbers would you like in your list? "))
        if vals <= 1:
            raise ValueError("You must enter more than 1 item.")

        print(f"\nEnter {vals} unique numbers for your list.\n")

        while len(mylist) < vals:
            try:
                val = float(input(f"Enter a number {len(mylist)+1}: "))
                if val in mylist:
                    print("Duplicate detected. Try a different number.\n")
                else:
                    mylist.append(val)
            except ValueError:
                print("Invalid input. Please enter a number.\n")

        mylist.sort()
        print(f"\nSorted list: {mylist}\n")

        target_input = input("Enter a number to search for, or type 'no' to let the computer choose randomly: ")
        if target_input.lower().strip() in ["no", "n"]:
            lower = random.randint(-1000, -1)
            upper = random.randint(1, 1000)
            mytarget = random.randint(lower, upper) if random.choice(["int", "float"]) == "int" else round(random.uniform(lower, upper), 2)
            print(f"\nComputer randomly chose: {mytarget} (range: {lower} to {upper})\n")
        else:
            try:
                mytarget = float(target_input)
            except ValueError:
                raise ValueError("Invalid target value.")

        result = binarySearch(mylist, mytarget)
        if result != -1:
            print(f"\nFound {mytarget} at index {result}\n")
        else:
            print(f"\n{mytarget} not found in the list.\n")

    except Exception as e:
        print(f"\nError: {e}\nPlease rerun the program and ensure all input is valid.\n")

def BubbleSorter():
    print("\nBubble Array Sorter\n")

    array = []
    vals = int(input("How many numbers would you like in your list? "))
    print(f"\nYou will be asked to enter {vals} numbers. No duplicates allowed.\n")

    while len(array) < vals:
        try:
            val = float(input(f"Enter a number {len(array)+1}: "))
            if val in array:
                print("Duplicate detected. Try a different number.\n")
            else:
                array.append(val)
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    for a in range(len(array) - 1):
        for b in range(len(array) - a - 1):
            if array[b] > array[b + 1]:
                array[b], array[b + 1] = array[b + 1], array[b]

    print("\nSorted array:")
    for i in array:
        print(f"{i}")
    print()

def InsertionSorter():
    print("\nThis lesson is under construction.\n")
def RadixSorter():
    print("\nThis lesson is under construction.\n")

def QuickSorter():
    print("\nQuick Sorter\n")

    array = []
    vals = int(input("How many numbers would you like in your list? "))
    print(f"\nYou will be asked to enter {vals} numbers. No duplicates allowed.\n")

    while len(array) < vals:
        try:
            val = float(input(f"Enter a number {len(array)+1}: "))
            if val in array:
                print("Duplicate detected. Try a different number.\n")
            else:
                array.append(val)
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    def partition(array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    def quicksort(array, low=0, high=None):
        if high is None:
            high = len(array) - 1
        if low < high:
            pivot_index = partition(array, low, high)
            quicksort(array, low, pivot_index - 1)
            quicksort(array, pivot_index + 1, high)

    quicksort(array)
    print("\nSorted array:")
    for val in array:
        print(f"{val}")
    print()

def MergeSorter():
    print("\nThis lesson is under construction.\n")

def SelectionSorter():
    print("\nSelection Sorter\n")

    mylist = []
    vals = int(input("How many numbers would you like in your list? "))
    print(f"\nYou will be asked to enter {vals} numbers. No duplicates allowed.\n")

    while len(mylist) < vals:
        try:
            val = float(input(f"Enter a number {len(mylist)+1}: "))
            if val in mylist:
                print("Duplicate detected. Try a different number.\n")
            else:
                mylist.append(val)
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    amt = len(mylist)
    for bgn in range(amt - 1):
        minidex = bgn
        for jr in range(bgn + 1, amt):
            if mylist[jr] < mylist[minidex]:
                minidex = jr
        mylist[bgn], mylist[minidex] = mylist[minidex], mylist[bgn]

    print("\nSorted array:")
    for val in mylist:
        print(f"{val}")
    print()

def CountingSorter():
    print("\nThis lesson is under construction.\n")
