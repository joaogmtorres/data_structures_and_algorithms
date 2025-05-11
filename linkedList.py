class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value} e {self.next}"

class LinkedList:
    def __init__(self):
        self.start = None

    def insert_in_end(self, value):
        new_node = Node(value)
        if self.start is None:
            self.start = new_node
        else:
            current_node = self.start
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def insert_in_start(self, value):
        new_node = Node(value)
        new_node.next = self.start
        self.start = new_node
    def __str__(self):
        current_node = self.start
        elements = []
        while current_node:
            elements.append(str(current_node.value))
            current_node = current_node.next
        return ",".join(elements) if elements else "Waiting the creation of list"



new_list = LinkedList()
new_list.insert_in_end(20)
new_list.insert_in_end(30)
print(new_list)
new_list.insert_in_start(10)
new_list.insert_in_end(40)
print(new_list)