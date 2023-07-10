## Recursion

def recursionsum(x):
    if x <= 0:
        return 0
    return x + recursionsum(x-1)


result1 = recursionsum(5)

print(result1)


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

result = factorial(5)

print(result)


#Utilities and Fonts


class Node:
    def __init__(self, valueInput="Default"):
        self.value = valueInput
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
    def newFront(self, value):
        if self.head == None:
            self.head == Node(value)
        else:
            runner = self.head
            while runner.next != None:
                self.head == self.next
                Node(value) == self.head

    def countNodes(self, count):
        if self.head == None:
            print("No values to count")
        else:
            runner = self.head
            while runner != None:
                count += 1
                runner = runner.next
            print(count)
            return count

    def contains(self, valueInput):
        if self.head == None:
            print("No Values in list")
        else:
            runner = self.head
            while runner != None:
                if runner.value == valueInput:
                    print("List contains value")
                    return self

                runner = runner.next
                print("Value not found in list")
                return self

    def length(self):
        if self.head == None:
            print("No values to Count")
        else:
            runner = self.head
            count = 0
            while runner != None:
                count = count+1
                runner = runner.next
            print(count)
            return count

    def displayValues(self):
        if self.hed == None:
            print("No Values")
        else:
            runner = self.head
            while runner != None:
                print(runner.value)
                runner = runner.next
        return self


##Binary Search Trees


class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, val):
        new_node = Node(val)
        if self.root == None:
            self.root = new_node
            return self
        runner = self.root
        while runner != None:
            if new_node.value <= runner.value:
                if runner.left == None:
                    runner.left = new_node
                    return self
                runner = runner.left
            else:
                if runner.right == None:
                    runner.right = new_node
                    return self
                runner = runner.left


    def printLeft(self):
        if self.root == None:
            return "This tree is empty"
        runner = self.root
        while runner.left != None:
            print(runner.value)
            runner = runner.left
        return self


    def min(self):
        if self.root == None:
            return "This tree is empty"
        runner = self.root
        min = self.root.value
        while runner.left != None:
            if runner.left < min:
                min = runner.left
            runner = runner.left
        return min

    def max(self):
        runner = self.root
        max = self.root.value
        while runner.right != None:
            if runner.right > max:
                max = runner.right
            runner = runner.right
        return max









