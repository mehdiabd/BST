class LinkList:

    def __init__(self, k):
        self.nextNode = None
        self.key = k
        self.prevNode = None

    def add(self, k):
        current = self
        if current.nextNode is not None:
            current.nextNode.add(k)
            return
        current.nextNode = LinkList(k)

    def show(self, val):
        current = self
        print(current.key)
        if current.nextNode is not None:
            current.nextNode.show(val)

    def merge_list(self, lst):
        current = self
        while current is not None:
            if current.key == lst.key:
                break
            elif current.nextNode is not None:
                current = current.nextNode
            else:
                current.nextNode = LinkList(lst.key)
        if lst.nextNode is not None:
            self.merge_list(lst.nextNode)
