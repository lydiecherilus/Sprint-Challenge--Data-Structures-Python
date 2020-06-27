import time

# Add a binary Search Tree to get the duplicates
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
    def insert(self, value):
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else: 
                self.right = BSTNode(value)  
        if value < self.value: 
            if self.left:
                self.left.insert(value)
            else: 
                self.left = BSTNode(value)
   

    def contains(self, target):
        if target == self.value:
            return duplicates.append(target)
        else:
            if target >= self.value:
                if self.right:
                    return self.right.contains(target)
                else:
                    return False
            else:
                if self.left:
                    return self.left.contains(target)
                else:
                    return False

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

# improvements
Binary_Tree = BSTNode(names_1[0]) 
for name_1 in names_1[1:]:
    Binary_Tree.insert(name_1)
 
for name_2 in names_2:
    Binary_Tree.contains(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# names_1 = set(line.strip() for line in open('names_1.txt'))
# names_2 = set(line.strip() for line in open('names_2.txt'))

# for line in names_1 & names_2:
#     if line:
#         print(line)