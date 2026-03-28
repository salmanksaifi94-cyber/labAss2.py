#   Name='Salman'
#   Roll_no=2501840005
#   LabASS=2



class DynamicArray:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * self.capacity

    def append(self, x):
        if self.size == self.capacity:
            print(f"Resizing from {self.capacity} to {self.capacity * 2}")
            self.capacity *= 2
            new_arr = [None] * self.capacity

            for i in range(self.size):
                new_arr[i] = self.arr[i]

            self.arr = new_arr

        self.arr[self.size] = x
        self.size += 1

    def pop(self):
        if self.size == 0:
            return "Array is empty"
        val = self.arr[self.size - 1]
        self.size -= 1
        return val

    def __str__(self):
        return str(self.arr[:self.size])
    

    # TASK2

    class Node:
       def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new

    def insert_end(self, x):
        new = Node(x)
        if not self.head:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def delete_value(self, x):
        temp = self.head
        if temp and temp.data == x:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != x:
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


    # double linklist

    class DNode:
       def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_after(self, target, x):
        temp = self.head
        while temp:
            if temp.data == target:
                new = DNode(x)
                new.next = temp.next
                new.prev = temp

                if temp.next:
                    temp.next.prev = new
                temp.next = new
                return
            temp = temp.next

    def delete_position(self, pos):  # 0-based
        if not self.head:
            return

        temp = self.head

        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        for i in range(pos):
            temp = temp.next
            if not temp:
                return

        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next

    # Task 3

    class Stack:
      def __init__(self):
        self.head = None

    def push(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new

    def pop(self):
        if not self.head:
            return "Empty"
        val = self.head.data
        self.head = self.head.next
        return val

    def peek(self):
        if not self.head:
            return "Empty"
        return self.head.data 
    
    class Queue: 
      def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new = Node(x)
        if not self.tail:
            self.head = self.tail = new
            return
        self.tail.next = new
        self.tail = new

    def dequeue(self):
        if not self.head:
            return "Empty"
        val = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

    def front(self):
        if not self.head:
            return "Empty"
        return self.head.data
    
# Task 4
def is_balanced(expr):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in "({[":
            stack.push(ch)
        elif ch in ")}]":
            if stack.head is None:
                return False
            if stack.pop() != pairs[ch]:
                return False

    return stack.head is None