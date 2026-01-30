"""
File Name: singly_linked_list.py

Purpose:
--------
This file contains the implementation of a Singly Linked List.
Each node stores data and a reference to the next node.

Operations supported:
- Insert at beginning
- Insert at end
- Delete a node
- Search a value
- Display the list

Time Complexity:
----------------
Insertion at beginning: O(1)
Insertion at end:       O(n)
Deletion:               O(n)
Search:                 O(n)

Space Complexity:
-----------------
O(n)
"""


class Node:
    def __init__(self, data):
        # Store data in the node
        self.data = data
        # Pointer to the next node
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        # Initialize head of the list
        self.head = None

    def insert_at_beginning(self, data):
        # Create a new node
        new_node = Node(data)
        # Point new node to current head
        new_node.next = self.head
        # Update head to new node
        self.head = new_node

    def insert_at_end(self, data):
        # Create a new node
        new_node = Node(data)

        # If list is empty, make new node the head
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the last node
        current = self.head
        while current.next:
            current = current.next

        # Link last node to new node
        current.next = new_node

    def delete(self, key):
        # Store head node
        current = self.head

        # If head node itself holds the key
        if current and current.data == key:
            self.head = current.next
            return

        # Search for the key
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If key not found
        if current is None:
            return

        # Unlink the node
        prev.next = current.next

    def search(self, key):
        # Start from head
        current = self.head

        # Traverse the list
        while current:
            if current.data == key:
                return True
            current = current.next

        return False

    def display(self):
        # Traverse and print the list
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# ------------------ Example Usage ------------------

ll = SinglyLinkedList()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)

ll.insert_at_beginning(5)

print("Linked List:")
ll.display()

print("Search 20:", ll.search(20))

ll.delete(20)
print("After deleting 20:")
ll.display()
