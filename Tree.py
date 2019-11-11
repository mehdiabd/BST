from linkList import LinkList


class Tree:
    def __init__(self, key, val):
        self.no = val
        self.left = None
        self.right = None
        self.lst = LinkList(key)
        self.max = self.no
        self.parent = None

    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.no)
        if self.right:
            self.right.in_order()

    def pre_order(self):
        output = str(self.no) + "("
        if self.left:
            output += 'L|' + self.left.pre_order()
        if self.right:
            output += 'R|' + self.right.pre_order()
        return output + ')'

    def insert(self, key, val):
        if val == self.no:
            if key != self.lst.key:
                self.lst.add(key)
        elif val < self.no:
            if self.left:
                self.left.insert(key, val)
            else:
                self.left = Tree(key, val)
                self.left.parent = self
        else:
            if self.right:
                self.right.insert(key, val)
                self.max = max(val, self.max)
            else:
                self.right = Tree(key, val)
                self.max = max(val, self.max)
                self.right.parent = self

    def mrg(self, tree):
        if self.no == tree.no:
            x = self.lst
            x.merge_list(tree.lst)
        elif self.no < tree.no:
            if self.right:
                self.right.mrg(tree)
                self.max = max(tree.no, self.max)
            else:
                self.right = Tree(tree.lst, tree.no)
                self.right.lst = tree.lst
                self.right.parent = self
                self.max = max(tree.no, self.max)
        else:
            if self.left:
                self.left.mrg(tree)
            else:
                self.left = Tree(tree.lst, tree.no)
                self.left.lst = tree.lst
                self.left.parent = self

    def merge(self, tree):
        self.mrg(tree)
        if tree.left:
            self.merge(tree.left)
        if tree.right:
            self.merge(tree.right)

    def nodes_max(self):
        print(self.no, '->', self.max)
        if self.left:
            self.left.nodes_max()
        if self.right:
            self.right.nodes_max()

    def show_list(self, val):
        current = self
        if val == current.no:
            current.lst.show(val)
        elif val < current.no:
            if current.left:
                current.left.show_list(val)
            else:
                print(" N O T  F O U N D ! ")
        else:
            if current.right:
                current.right.show_list(val)
            else:
                print(" N O T  F O U N D ! ")

    def remove(self, inp):
        if inp < self.max:
            self.rmv(inp)
            print(self.pre_order())
        else:
            print("Can't Remove The Max Or Above !")
            return False

    def rmv(self, inp):
        if self.no == inp:
            if self.right is not None:
                self.no = self.right.no
                left_node = self.right.left
                self.right = self.right.right
                self.left = left_node
            else:
                if self.parent is not None:
                    if self.no == self.parent.left.no:
                        self.left = None
                        self.parent.left = None
                        return
                    elif self.no == self.parent.right.no:
                        self.parent.parent.left = None
                else:
                    print("STh Went Wrong :(")

        elif self.no < inp:
            if self.right is not None:
                self.no = self.right.no
                left_node = self.right.left
                self.right = self.right.right
                self.left = left_node
                return self.rmv(inp)
            else:
                print("Not Found !")
                return False

        else:
            if self.left:
                self.left.rmv(inp)
            else:
                print("Not Found !")
                return False
