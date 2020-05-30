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
        # set initial head to current
        current = self.head
        # set initial node prior to head (old) to None
        old = None
        # loop while current is not none (current is set to next_node each loop which eventually becomes None)
        while current:
            # set next node to current's next_node attribute
            next = current.next_node
            # set current's next_node reference to old (reversing the next reference)
            current.next_node = old
            # set old node reference to current
            old = current
            # set current node reference to next in preparation to start next loop
            current = next
        # reset head to the latest old which will be the very last node
        self.head = old

        # before: old => current => next_node
        # now: next_node (old) => current => old (next_node)
