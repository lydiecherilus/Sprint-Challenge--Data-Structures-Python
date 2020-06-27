class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node is None:
            return None
        else:
            if node.get_next() == None:
                self.head = node
                self.head.next_node = prev
                return
            self.reverse_list(node.get_next(), node)
            node.next_node = prev

    def print(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next_node

print_test = LinkedList()
print_test.add_to_head(1)
print_test.add_to_head(2)
print_test.add_to_head(3)

print_test.print()
print_test.reverse_list(None, None)