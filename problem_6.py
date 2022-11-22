# Union and Intersection
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

def intersectionPoint(head1, head2):
    pt1, pt2 = head1, head2

    if (head1 == None or head2 == None):
        return None
    
    # o(n) algorithm time, O(n) space.
    set1 = set()
    intersectionSet = set()
    
    while pt1!=None:
        set1.add(pt1.value)
        pt1 = pt1.next
    
    while pt2!=None:
        if pt2.value in set1:
            intersectionSet.add(pt2.value)
        pt2 = pt2.next
        
    def makeLinkedList(intersectionSet):
        head = temp = Node()
        for val in intersectionSet:
            temp.value = value
            temp = temp.next
        return head
    
    return makeLinkedList(intersectionSet)

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,3,11,21,1]

temp1 = head1 = Node(0)
temp2 = head2 = Node(0)
for i in element_1:
    temp1.value = value
    temp1 = temp1.next

for i in element_2:
    temp2.value = value
    temp2 = temp2.next

#print (union(linked_list_1,linked_list_2))
print(intersectionPoint(temp1.next, temp2.next))

def union(head1, head2):
    return 1

# def union(head1, head2):
#     answer = linkedlist()
#     pointer1 = head1
#     pointer2 = head2
#     while pointer1:
#         answer.add(pointer1.val)
#         pointer1 = pointer1.next
        
#     while pointer2:
#         answer.add(pointer2.val)
#         pointer2 = pointer2.next
#     return answer
