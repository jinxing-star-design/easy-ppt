class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    def __str__(self):
        return '<{} -> {}>'.format(self.item,
                                   self.next.item if self.next else 'None')


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.items = []

    def append(self, item):
        node = Node(item)

        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

        self.items.append(node)
        return self

    def get(self, index):
        return self.items[index]

    def iternodes(self):
        # current = self.head
        # while current:
        #     yield current
        #     current = current.next
        yield from self.items


ll = LinkedList()
ll.append(1)
ll.append(2).append(3)

for x in ll.iternodes():
    print(x)
