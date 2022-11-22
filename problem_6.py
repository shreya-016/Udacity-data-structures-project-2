# Union and Intersection
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.size += 1
            return

        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def get_size(self):
        return self.size

    def __str__(self):
        node = self.head
        out_string = ""
        while node:
            out_string += str(node.value) + " -> "
            node = node.next
        out_string += 'None'  
        return out_string


def copyLinkedList(l1, newlist):
    l1Set = getL1Set(l1)

    node = newlist.head
    while(node):
        value = node.value
        if value not in l1Set:
            l1.append(value)
            l1Set.add(value)
        node = node.next

def union(l1, l2):
    ansList = LinkedList()

    if l1.get_size() == 0:
        copyLinkedList(ansList, l2)
        return ansList
    else:
        copyLinkedList(ansList, l1)

    if l2.get_size() == 0:
        return ansList
    else:
        copyLinkedList(ansList, l2)

    return ansList


def getL1Set(l1):
    l1Set = set()

    node = l1.head
    while node:
        l1Set.add(node.value)
        node = node.next

    return l1Set


def intersection(l1, l2):
    ansList = LinkedList()
    if l1.get_size() == 0 or l2.get_size() == 0:
        return ansList 

    newlistSet = getL1Set(l1)

    node = l2.head
    while node:
        if node.value in newlistSet:
            ansList.append(node.value)
        node = node.next

    return ansList


def test(linked_list_1, linked_list_2):
    print(f'Set 1: {linked_list_1}')
    print(f'Set 2: {linked_list_2}')
    print(f'Union: {union(linked_list_1, linked_list_2)}')
    print(f'Intersection: {intersection(linked_list_1, linked_list_2)}')
    print()


# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

test(linked_list_1, linked_list_2)

# Test case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

test(linked_list_3, linked_list_4)


# Test case 3
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()
element = [1, 2, 3, 4, 5, 6, 7]

for i in element:
    linked_list_6.append(i)

test(linked_list_5, linked_list_6)


# Test case 4
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()
element7 = [1, 2, 3, 4, 5, 6, 7]
element8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in element7:
    linked_list_7.append(i)

for i in element8:
    linked_list_8.append(i)

test(linked_list_7, linked_list_8)


# Test case 5
linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

test(linked_list_9, linked_list_10)
