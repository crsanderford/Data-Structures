"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

   unlike arrays, singly linked lists aren't symmetric, so choosing to add to and remove from
   the head or the tail has performance consequences.
"""

from singly_linked_list import LinkedList

# singly-linked-list version
class Stack:
    def __init__(self):

        self.size = 0
        self.storage = LinkedList()

    def __len__(self):

        return self.size

    def push(self, value):

        self.storage.add_to_head(value)
        self.size +=1

    def pop(self):
        
        if self.size <= 0:
            return None

        else:
            val = self.storage.head.get_value()
            self.storage.remove_head()
            self.size -= 1

            return val


"""# array version
class Stack:
    def __init__(self):

        self.size = 0
        self.storage = []

    def __len__(self):

        return self.size

    def push(self, value):

        self.storage.append(value)
        self.size +=1

    def pop(self):
        if self.size <= 0:
            return None
        
        else:
            self.size -= 1
            return self.storage.pop()"""
