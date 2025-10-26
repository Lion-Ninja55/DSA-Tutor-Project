import secondary

print(f"\n{'DSA Tutor':^30}")
print(f"{'_' * 30}\n")

print("\nThis program will help you learn DSA. It is an interactive program designed for educational purposes.\n")
print("This course helps you learn through lessons, exercises, quizzes, tests, study guides, and projects.\n")
print("Hope you enjoy it!\n")

print("\nLet's begin! I will start with the first lesson. Always pay attention, and you may succeed.\nLet's get started.\n")
print("DSA stands for Data Structures and Algorithms.\n")

topics = ['Arrays Ex.', 'Minimum Value Finder Ex.', 'Binary Search Ex.', 'Bubble Sort Ex.', 'Insertion Sort Ex.', 'Radix Sort Ex.', 'Quick Sort Ex.',
          'Merge Sort Ex.', 'Selection Sort Ex.', 'Counting Sort Ex.']

examples = ['Arrays Ex.', 'Minimum Value Finder Ex.', 'Binary Search Ex.', 'Bubble Sort Ex.', 'Insertion Sort Ex.', 'Radix Sort Ex.', 'Quick Sort Ex.',
            'Merge Sort Ex.', 'Selection Sort Ex.', 'Counting Sort Ex.']

while True:
    print("\nAvailable Topics:\n")
    for i, topic in enumerate(topics, 1):
        print(f"\n{i}. {topic}")
    print("""\n0. Exit

(Program will stop when 0 is pressed, otherwise keep running forever)\n""")

    try:
        pick = int(input("\nPick a topic by entering its number (0 to exit): ").strip())

        if pick == 0:
            print("\nThanks for learning with DSA Tutor! See you next time.\n")
            break

        elif pick == 1:
            print("\nArrays are like lists. Many operations can be performed on them, such as sorting and other manipulations.\n"
                  "They can store multiple data types and are considered a data structure. In Python, arrays are similar to lists.\n")

        elif pick == 2:
            print("\nMinimum Value Finder is a basic algorithm to find the smallest value in an array. Here's how:\n"
                  "1. Create a variable 'minVal' and set it to the first element.\n"
                  "2. Traverse the array.\n"
                  "3. If a smaller value is found, update 'minVal'.\n"
                  "4. After the loop, 'minVal' holds the smallest value.\n")

        elif pick == 3:
            print("\nBinary Search is used to find a number or value in a sorted array. It's an algorithm—the 'A' in DSA.\n"
                  "How it works:\n"
                  "1. Check the value in the center of the array.\n"
                  "2. If the target value is lower, search the left half. If higher, search the right half.\n"
                  "3. Repeat until found or the search area is empty.\n"
                  "4. Return the index if found, or -1 if not.\n")

        elif pick == 4:
            print("\nBubble Sort is a sorting algorithm. Here's how it works:\n"
                  "1. Go through the array one value at a time.\n"
                  "2. Compare each value with the next.\n"
                  "3. If the current value is greater, swap them.\n"
                  "4. Repeat for the entire array.\n")

        elif pick == 5:
            print("\nInsertion Sort works like this:\n"
                  "1. Take the first value from the unsorted part.\n"
                  "2. Insert it into the correct position in the sorted part.\n"
                  "3. Repeat for all values.\n")

        elif pick == 6:
            print("\nRadix Sort is a digit-based sorting algorithm. Here's how it works:\n"
                  "1. Start with the least significant digit.\n"
                  "2. Sort values into buckets based on that digit.\n"
                  "3. Reassemble the array from the buckets.\n"
                  "4. Repeat for each digit until sorted.\n")

        elif pick == 7:
            print("\nQuick Sort is a fast sorting algorithm. Here's how it works:\n"
                  "1. Choose a pivot element.\n"
                  "2. Place lower values to the left and higher to the right.\n"
                  "3. Swap the pivot into its correct position.\n"
                  "4. Recursively apply the same steps to sub-arrays.\n")

        elif pick == 8:
            print("\nMerge Sort is another sorting algorithm. Here's how it works:\n"
                  "1. Divide the array into two halves.\n"
                  "2. Keep dividing until each sub-array has one element.\n"
                  "3. Merge sub-arrays by placing the lowest value first.\n"
                  "4. Continue merging until the array is sorted.\n")

        elif pick == 9:
            print("\nSelection Sort works as follows:\n"
                  "1. Find the lowest value in the array.\n"
                  "2. Move it to the front of the unsorted part.\n"
                  "3. Repeat for the remaining elements.\n")

        elif pick == 10:
            print("\nCounting Sort is a simple and efficient algorithm. Here's how it works:\n"
                  "1. Create a new array to count occurrences of each value.\n"
                  "2. Traverse the original array and update the count array.\n"
                  "3. Use the count array to reconstruct the sorted array.\n")

        else:
            print(f"\nError: '{pick}' is not a valid number. Please choose a number between 0 and 10.\n")

        print("\nNow let's do more learning\n")
        print("\nOkay, so I'll give you the list again but this time you'll be asked for a list, and that sort will be applied to that list!")

        print("\nAvailable Topic Examples:\n")
        for i, example in enumerate(examples, 11):
            print(f"\n{i}. {example}")
        print("""\n0. Exit

(Program will stop when 0 is pressed, otherwise keep running forever)\n""")

        choice = int(input('Pick a choice to see the practical example of it in work (0 to exit): ').strip())

        if choice == 0:
            print("\nThanks for learning with DSA Tutor! See you next time.\n")
            break

        elif choice == 11:
            secondary.ArraysLesson()
        elif choice == 12:
            secondary.MinValFind()
        elif choice == 13:
            secondary.BinarySearcher()
        elif choice == 14:
            secondary.BubbleSorter()
        elif choice == 15:
            secondary.InsertionSorter()
        elif choice == 16:
            secondary.RadixSorter()
        elif choice == 17:
            secondary.QuickSorter()
        elif choice == 18:
            secondary.MergeSorter()
        elif choice == 19:
            secondary.SelectionSorter()
        elif choice == 20:
            secondary.CountingSorter()

    except ValueError:
        print("\nInvalid input. Please enter a proper input.\n")

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}\nPlease try again.\n")