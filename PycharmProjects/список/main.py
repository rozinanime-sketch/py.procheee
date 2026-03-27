class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # вставка в голову
    def insert(self, data):
        """Insert a new node at the beginning of the list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # вставка в хвост
    def append(self, data):
        """Insert a new node at the end of the list"""
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    # удалить из головы
    def remove(self):
        """Delete the first node from the list"""
        if not self.head:
            return

        self.head = self.head.next

    # удалить из хвоста
    def delete(self):
        """Delete the last node from the list"""
        if not self.head:
            return

        if not self.head.next:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next

        current.next = None

    # размер списка
    def size(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count

    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))


# Example usage:
if __name__ == "__main__":
    l = LinkedList()

    # Insert elements
    l.append(10)
    l.append(20)
    l.append(30)
    l.insert(5)

    l.print_list()  # 5 -> 10 -> 20 -> 30

    # Delete from head
    l.remove()
    l.print_list()  # 10 -> 20 -> 30

    # Delete from tail
    l.delete()
    l.print_list()  # 10 -> 20




