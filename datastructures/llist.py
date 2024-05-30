class llist_node:
    def __init__(self, value, next, prev):
        self.value =  value
        self.next = next
        self.prev = prev

class llist:
    def __init__(self):
        self.front  : llist_node = None
        self.back   : llist_node= None
        self.size   : int = 0

    def append(self, value):
        new_node = llist_node(value, None, None)
        