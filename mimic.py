class Node(object):

    def __init__(self, data, next_node=None):
        self.next_node = next_node
        self.data = data

    def delete_next_node(self):
        self.next_node = self.next_node.next_node


class MyList(object):

    def __init__(self):
        self.length = 0
        self.first_node = None

    def __len__(self):
        return self.length

    def __iter__(self):
        return NodeIterator(self)

    def __getitem__(self, key: int):
        return self._get_node(key).data

    def __add__(self, other):
        extended = self.copy()
        extended.extend(other)
        return extended

    def _get_node(self, key: int) -> Node:
        current = self.first_node
        i = 0
        while current:
            if i == key:
                return current
            i += 1
            current = current.next_node

    def append(self, value):
        self.insert(len(self) - 1, value)

    def count(self, value):
        return sum(1 for i in self if i == value)

    def index(self, value):
        for i, current_value in enumerate(self):
            if current_value == value:
                return i

    def clear(self):
        self.first_node = None
        self.length = 0

    def copy(self):
        new = MyList()
        for value in self:
            new.append(value)
        return new

    def extend(self, other):
        for i in other:
            self.append(i)

    def insert(self, index: int, value):
        if index <= 0:
            self.first_node = Node(value, self.first_node)
        else:
            prev_node = self._get_node(index - 1)
            prev_node.next_node = Node(value, prev_node.next_node)
        self.length += 1

    def pop(self, index: int):
        if index == 0:
            poped_node = self.first_node
            self.first_node = self.first_node.next_node
        else:
            prev_node = self._get_node(index - 1)
            poped_node = prev_node.next_node
            prev_node.delete_next_node()
        self.length -= 1
        return poped_node.data

    def remove(self, value):
        index = self.index(value)
        self.pop(index)

    def reverse(self):
        new = MyList()
        for i in range(len(self) - 1, -1, -1):
            new.append(self[i])
        self.first_node = new.first_node

    def sort(self):
        l = sorted(self)
        self.clear()
        self.extend(l)

    def __repr__(self):
        return str([i for i in self])

    def __str__(self):
        return self.__repr__()


class NodeIterator(object):

    def __init__(self, my_list: MyList):
        self.current = my_list.first_node

    def __next__(self):
        if not self.current:
            raise StopIteration()
        current = self.current
        self.current = self.current.next_node
        return current.data


if __name__ == '__main__':
    l = MyList()
    print(dir(l))
    l.append('a')  # not in correct order!
    l.append('b')
    l.append('c')
    l.append('a')
    print(l)  # [a, b, c, a]
    l2 = l.copy()
    print(l2 is l)  # False
    print(l2)  #[a, b, c, a]
    l2.clear()
    print(l2)  #[]
    print(l2.count('a'))  # 2
    l.extend(['d', 'e'])
    print(l)  # [abcde]
    print(l.index('d'))  # 4
