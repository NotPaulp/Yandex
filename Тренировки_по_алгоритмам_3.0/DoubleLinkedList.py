
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    def delete_at_head(self):
        if self.is_empty():
            raise IndexError("Linked list is empty")
        if self.head == self.tail:
            data = self.head.data
            self.head = None
            self.tail = None
        else:
            data = self.head.data
            self.head = self.head.next
            self.head.prev = None
        return data

    def delete_at_tail(self):
        if self.is_empty():
            raise IndexError("Linked list is empty")
        if self.head == self.tail:
            data = self.tail.data
            self.head = None
            self.tail = None
        else:
            data = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
        return data

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()
list1=DoublyLinkedList()
list1.insert_at_head(1)
list1.insert_at_tail(2)
list1.display_forward()