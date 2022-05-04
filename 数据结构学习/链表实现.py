from ast import increment_lineno
from itertools import count
from xml.dom import NoDataAllowedErr


class Node(object):
    def __init__(self, item) -> None:
        self.item = item
        self.next = None
        self.prev = None

class DLinkList(object):
    def __init__(self) -> None:
        self.head = None
    def is_empty(self) -> bool:
        return self.head is None
    def get_length(self):
        cur = self.head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count
    def trabel(self):
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next
    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur