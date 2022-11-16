class Node:
    def __init__(self, data):
        self.item = data
        self.next_item = None
        self.index = None


class List:
    size = 0

    def __init__(self):
        self.start_node = Node(None)

    def new_index(self, node):
        node.index = self.size
        self.size += 1

    def is_empty(self):
        return self.size == 0

    def add(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.start_node = new_node
        else:
            current_node = self.start_node
            while current_node.next_item is not None:
                current_node = current_node.next_item
            current_node.next_item = new_node
        self.new_index(new_node)

    def get(self, element_index):
        if element_index > self.size - 1:
            raise NameError('index out of range')
        current_node = self.start_node
        while current_node.index != element_index:
            current_node = current_node.next_item
        return current_node.item

    def print(self):
        if self.size == 0:
            print('This list is empty.')
            return
        current_node = self.start_node
        print('[', end='')
        while current_node.next_item is not None:
            print(current_node.item, end=', ')
            current_node = current_node.next_item
        print(f'{current_node.item}]')

    def contains(self, data):
        current_node = self.start_node
        while current_node.next_item is not None:
            if current_node.item == data:
                return True
            current_element = current_node.next_item
        return current_node.item == data

    def get_node_by_index(self, element_index):
        if element_index > self.size - 1:
            raise NameError('index out of range')
        current_node = self.start_node
        while current_node.index != element_index:
            current_node = current_node.next_item
        return current_node

    def delete_by_index(self, element_index):
        if element_index == 0:  # delete first element from the list
            if self.size - 1:
                current_node = self.start_node
                self.start_node = self.get_node_by_index(1)
            else:
                self.start_node = Node(None)
                self.size -= 1
                return

        elif element_index == self.size - 1:  # delete last element from the list
            self.get_node_by_index(element_index - 1).next_item = None
            self.size -= 1
            return

        else:  # delete not the first and not the last element of the list
            current_node = self.get_node_by_index(element_index - 1)
            current_node.next_item = self.get_node_by_index(element_index + 1)

        while current_node.next_item is not None:  # change all the index
            current_node.next_item.index -= 1
            current_node = current_node.next_item
        self.size -= 1

    def sort(self):
        def quick_sort(lst):
            if len(lst) <= 1:
                return lst
            pivot = lst[int(len(lst) / 2)]
            left = list(filter(lambda elem: elem < pivot, lst))
            center = [elem for elem in lst if elem == pivot]
            right = list(filter(lambda elem: elem > pivot, lst))
            return quick_sort(left) + center + quick_sort(right)

        items_list = []
        for index in range(self.size):
            items_list.append(self.get(index))
        sorted_items = quick_sort(items_list)
        for index in range(self.size):
            self.get_node_by_index(index).item = sorted_items[index]


my_list = List()
my_list.add(43)
my_list.add(22)
my_list.add(11)
my_list.add(1003)
my_list.add(456)
my_list.print()
my_list.sort()
my_list.print()