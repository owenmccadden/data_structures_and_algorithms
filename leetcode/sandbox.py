# create a class to represent a binary tree node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_left(self, data):
        self.left = BinaryTreeNode(data)
        return self.left
    
    def insert_right(self, data):
        self.right = BinaryTreeNode(data)
        return self.right
    
    # create a method for a bread first search of the tree
    def bfs(self):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            print(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    

# create a binary tree with the following values:
# level 1: 1
# level 2: 3, 2
# level 3: 5, 3, 9

example = BinaryTreeNode(1)
example.insert_left(3)
example.insert_right(2)
example.left.insert_left(5)
example.left.insert_right(3)
example.right.insert_right(9)
# example.bfs()

# create a binary tree with the following values:
# level 1: 1
# level 2: 0, 1
# level 0: 0, 0, 1

example_2 = BinaryTreeNode(1)
example_2.insert_left(0)
example_2.insert_right(1)
example_2.right.insert_left(0)
example_2.right.insert_right(0)
example_2.left.insert_left(0)
example_2.left.insert_right(1)
example_2.bfs()

# create an example bianary tree with ten nodes all with the value 1

example_3 = BinaryTreeNode(1)
example_3.insert_left(1)
example_3.insert_right(1)
example_3.right.insert_left(1)
example_3.right.insert_right(1)
example_3.right.right.insert_left(1)
example_3.right.right.insert_right(1)
example_3.right.right.right.insert_left(1)
example_3.right.right.right.insert_right(1)
example_3.right.right.right.right.insert_right(1)
example_3.right.right.right.right.right.insert_right(1)
example_3.right.right.right.right.right.right.insert_right(1)
example_3.right.right.right.right.right.right.right.insert_right(1)



def get_rows(root):
    rows = []
    if root is None:
        return rows
    fill_rows(root, rows, 0)
    return rows

def fill_rows(root, rows, level):
    if root is None:
        return
    if len(rows) == level:
        rows.append([])
        rows[level].append(root.data)
    else:
        rows[level].append(root.data)
    fill_rows(root.left, rows, level + 1)
    fill_rows(root.right, rows, level + 1)

# create a class to represent a singly linked list node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # create a method to insert a new node at the end of the list
    def insert(self, data):
        new_node = Node(data)
        current = self
        while current.next is not None:
            current = current.next
        current.next = new_node
        return self
    
    # create a method to create a list from a list of integers

    def build_list(self, integers):
        for i in integers:
            self.insert(i)
        return self

    # create a method to print the list

    def print_list(self):
        current = self
        while current is not None:
            print(current.data)
            current = current.next

# create a sample linked list with 10 nodes with random values between 1 and 100

sample = Node(1)
sample.build_list([24,21,1,5,31,2,7,8,5])
sample.print_list()


# given an array of integers, d and an integer threshold t, return the number of triplets (a, b, c) that satisfy the following conditions:
    # d[a] + d[b] + d[c] <= t
    # d[a] < d[b] < d[c]
# return the number of triplets without using brute force

def triplets(t,d):
    count = 0
    for i in range(len(d)):
        for j in range(i+1, len(d)):
            for k in range(j+1, len(d)):
                if d[i] + d[j] + d[k] <= t and d[i] < d[j] < d[k]:
                    count += 1
    return count




# iterate from 10 to 1 and print the number

for i in range(10,0,-1):
    print(i)

# given a dictionary of nums, return the key of the max value of the dictionary:

def get_max_key(d):
    max_key = None
    max_value = None
    for key, value in d.items():
        if max_value is None or value > max_value:
            max_key = key
            max_value = value
    return max_key
    

# create a binary tree node class

class TreeNode(val=0, left=None, right=None):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def insert_left(self, data):
        self.left = TreeNode(data)
        return self.left
    
    def insert_right(self, data):
        self.right = TreeNode(data)
        return self.right

    def preorder(self):
        print(self.val)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()


# create a binary tree with the following values:
# level 1: 1
# level 2: 2, 5
# level 3: 3, 4, 6

example = TreeNode(1)
example.insert_left(2)
example.insert_right(5)
example.left.insert_left(3)
example.left.insert_right(4)
example.right.insert_right(6)




    
