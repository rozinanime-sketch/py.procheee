class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        """Вставить узел в голову"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        """Вставить узел в хвост"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove(self):
        """Удалить узел из головы"""
        if not self.head:
            return None
        removed = self.head.data
        self.head = self.head.next
        return removed

    def delete(self):
        """Удалить узел из хвоста"""
        if not self.head:
            return None
        if not self.head.next:
            removed = self.head.data
            self.head = None
            return removed
        current = self.head
        while current.next and current.next.next:
            current = current.next
        removed = current.next.data
        current.next = None
        return removed

    def size(self):
        """Длина списка"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

# Тестирование
if __name__ == "__main__":
    lst = LinkedList()
    lst.append(1)
    lst.insert(0)
    lst.append(2)
    print(lst.size())            # 3
    print(lst.remove())          # 0
    print(lst.delete())          # 2
    print(lst.size())            # 1
    print(lst.delete())          # 1
    print(lst.delete())          # None
