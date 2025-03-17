import numpy as np
import heapq
from collections import deque
import matplotlib.pyplot as plt
#1.calculator menu driven with match
def calculator():
    while True:
        print("\nMenu-Driven Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = int(input("Enter your choice (1-5): "))

        if choice == 5:
            print("Exiting")
            break

        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        match choice:
            case 1:
                print(f"Result: {a} + {b} = {a + b}")
            case 2:
                print(f"Result: {a} - {b} = {a - b}")
            case 3:
                print(f"Result: {a} * {b} = {a * b}")
            case 4:
                print(f"Result: {a} / {b} = {a / b if b != 0 else 'Undefined'}")
            case _:
                print("Invalid choice! Please enter a number between 1 and 5.")

calculator()

#2.N dimentional array  and perform addition subtration and multiplication
arr1 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
arr2 = np.array([[[9, 10], [11, 12]], [[13, 14], [15, 16]]])

print("Array 1:\n", arr1)
print("Array 2:\n", arr2)

# Addition
addition_result = arr1 + arr2
print("\nAddition:\n", addition_result)

# Subtraction
subtraction_result = arr1 - arr2
print("\nSubtraction:\n", subtraction_result)

#  Multiplication(Element-wise)
multiplication_result = np.multiply(arr1, arr2)
print("\nElement-wise Multiplication:\n", multiplication_result)

#  Multiplication(Matrix)
dot_product = np.matmul(arr1, arr2)
print("\nMatrix Multiplication:\n", dot_product)
#exploring DSA and its properties in python 
# 1️ List - Ordered, Mutable, Allows Duplicates
lst = [1, 2, 3, 4, 2, 5]
lst.append(6)  # Add element
lst.insert(2, 10)  # Insert at index 2
lst.remove(2)  # Remove first occurrence of 2
lst.pop()  # Remove last element
lst.sort()  # Sort list
print("List:", lst)

# 2️ Tuple - Ordered, Immutable, Allows Duplicates
tup = (1, 2, 3, 4, 2, 5)
print("Tuple:", tup)
print("Element at index 1:", tup[1])

# 3️ Set - Unordered, Unique Elements
st = {1, 2, 3, 4, 2, 5}
st.add(6)  # Add element
st.remove(3)  # Remove element
print("Set:", st)
print("Union:", st | {7, 8})  # Union
print("Intersection:", st & {2, 4, 6})  # Intersection

# 4️ Dictionary - Key-Value Pairs
dct = {'a': 1, 'b': 2, 'c': 3}
dct['d'] = 4  # Add new key-value pair
del dct['b']  # Remove a key
print("Dictionary:", dct)
print("Keys:", dct.keys())
print("Values:", dct.values())

# 5️ Stack (LIFO) - Using List
stack = []
stack.append(1)  # Push
stack.append(2)
stack.append(3)
print("Stack before pop:", stack)
stack.pop()  # Pop
print("Stack after pop:", stack)

# 6️ Queue (FIFO) - Using deque
queue = deque()
queue.append(1)  # Enqueue
queue.append(2)
queue.append(3)
print("Queue before dequeue:", queue)
queue.popleft()  # Dequeue
print("Queue after dequeue:", queue)

# 7️ Heap (Priority Queue) - Using heapq
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
print("Heap:", heap)
print("Smallest element:", heapq.heappop(heap))

# 8️ Deque (Double-Ended Queue)
dq = deque([1, 2, 3])
dq.appendleft(0)  # Insert at beginning
dq.append(4)  # Insert at end
print("Deque:", dq)
dq.pop()  # Remove from end
dq.popleft()  # Remove from beginning
print("Deque after removal:", dq)


# 9️ Linked List - Implemented using Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


ll = LinkedList()
ll.insert(3)
ll.insert(2)
ll.insert(1)
print("Linked List:")
ll.display()

# 5.read content from CSV and add  content  or tuple at begging ,middle and end

new_tuple = ('Eve', 22)
with open('data.csv', 'r', newline='') as file:
    reader = list(csv.reader(file))  # Convert to list
reader.insert(1, list(new_tuple))  # Insert at the beginning (after header)
if len(reader) > 2:  # Ensure at least two data rows exist before inserting in the middle
    middle_index = len(reader) // 2
    reader.insert(middle_index, list(new_tuple))  # Insert in the middle
reader.append(list(new_tuple))  # Insert at the end
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(reader)
with open('data.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#DATA.csv
Name,Age
Eve,22
Eve,22
Alice,25
Bob,30
Eve,22

# 6.crate bar chart and scatter plot for two dataset and use differnet colors  for  the  dataset in single wrap

# Scatter Plot Data
x1, y1 = np.random.rand(10), np.random.rand(10)
x2, y2 = np.random.rand(10), np.random.rand(10)

# Bar Chart Data
categories = ['A', 'B', 'C', 'D', 'E']
values1 = np.random.randint(1, 10, size=len(categories))
values2 = np.random.randint(1, 10, size=len(categories))

fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].scatter(x1, y1, color='red', label='Dataset 1')
axs[0].scatter(x2, y2, color='blue', label='Dataset 2')
axs[0].set_xlabel("X-axis")
axs[0].set_ylabel("Y-axis")
axs[0].set_title("Scatter Plot with Different Colors")
axs[0].legend()

bar_width = 0.4  # Width of bars
x = np.arange(len(categories))  # X positions for bars

axs[1].bar(x - bar_width/2, values1, width=bar_width, color='red', label='Dataset 1')
axs[1].bar(x + bar_width/2, values2, width=bar_width, color='blue', label='Dataset 2')

axs[1].set_xlabel("Categories")
axs[1].set_ylabel("Values")
axs[1].set_title("Bar Chart with Different Colors")
axs[1].set_xticks(x)
axs[1].set_xticklabels(categories)  # Set category labels on x-axis
axs[1].legend()

plt.tight_layout()
plt.show()






