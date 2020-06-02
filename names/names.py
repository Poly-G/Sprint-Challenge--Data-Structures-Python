import time
from collections import Counter

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# code pasted from prev projects


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        if value >= self.value:
            # check if right exists
            if self.right:
                # if so, make that node call insert with the same value
                self.right.insert(value)
            # if not, create a node with that value, set node as right child
            else:
                new_node = BSTNode(value)
                self.right = new_node

        else:
            if self.left:
                self.left.insert(value)

            else:
                new_node = BSTNode(value)
                self.left = new_node

        type(self.value) == 'number'

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        if target >= self.value:
            if self.right:
                self.right.contains(target)
            else:
                return False

        else:
            if self.left:
                return self.left.contains(target)
            else:
                return False


# counter
counter1 = Counter(names_1)
counter2 = Counter(names_2)

for key in counter1:
    if key in counter2:
        duplicates.append(key)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
