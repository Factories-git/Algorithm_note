class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def get_node(self, index):
        node = self.head
        c = 0
        while c < index:
            c += 1
            node = node.next
        return node

    def insert(self, value, index=None):
        if index is None:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(value)
        elif index == 0:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        else:
            prev_node = self.get_node(index - 1)
            new_node = Node(value)
            new_node.next = prev_node.next
            prev_node.next = new_node

    def delete_Node(self, index):
        if index == 0:
            del_node = self.head.data
            self.head = self.head.next
            return del_node
        node = self.get_node(index - 1)
        del_node = node.next.data
        node.next = node.next.next
        return del_node