class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        if self.next:
            return f'{self.data}->{self.next}'
        else:
            return f'{self.data}->|'


class DoubleLinkedList:
    def __init__(self):
        self.head: Node = None
        self.end: Node = None

    def push(self, data):
        new = Node(data)
        if not self.head:
            self.head, self.end = new, new
        else:
            self.end.next = new
            new.previous = self.head
            self.end = new
        return

    def pop(self):
        if not self.head:
            raise IndexError
        if not self.head.next:
            res = self.head.data
            self.head = None
            return res
        else:
            cur = self.head.next
            prev = self.head
            while cur.next is not None:
                prev = cur
                cur = cur.next
            res = cur.data
            prev.next = None
            return res

    def lenght_list(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def index(self, index):
        if not self.head:
            raise IndexError
        cur = self.head
        count = 0
        while cur != None:
            if count == index:
                return cur.data
            count += 1
            cur = cur.next

    def slice(self, index_1, index_2):
        rez = DoubleLinkedList()
        cur = self.head
        indx = 0
        while cur.next and indx < index_1:
            cur = cur.next
            indx += 1
        while indx <= index_2:
            rez.push(cur.data)
            indx += 1
            cur = cur.next
        return rez

    def remove(self, data) -> bool:
        cur = self.head
        prev = None
        while cur:
            if cur.data == data:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return True
            else:
                prev = cur
                cur = cur.next
        return False

    def insert(self, index, data):
        new = Node(data)
        cur = self.head
        prev = None
        count = 0
        while cur:
            if count == index:
                if prev:
                    prev.next = new
                    new.next = cur
                    cur = new
                    break
                else:
                    self.end.previous = new
                    new.next = self.head
                    new.previous = None
                    self.head = new
                    return True
            else:
                count += 1
                prev = cur
                cur = cur.next
        return False


if __name__ == '__main__':
    s = DoubleLinkedList()
    s.push(1)
    s.push(2)
    s.push(31)
    s.push(8)
    s.push(23)
    s.insert(2, 99)
    print(s.head)
    s.remove(23)
    print(s.head)
    s.slice(1,2)



