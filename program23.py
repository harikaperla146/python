#WAPP to delete asingle value from a link list
class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
def deleteNode(llist, position):
    if position == 0:
        #if deleting the head node, uodate the head to the next node
        llist = llist.next
    else:
        current = llist
        for _ in range(position - 1):
            #traverse to the node before the one to be deleted
            current = current.next
        #skip the node to be deleted
        current.next = current.next.next
    return llist
def printLinkedList(llist):
    current = llist
    while current is not None:
        print(current.data)
        current = current.next
#example usage
n= 8
elements = [20, 6, 2, 19, 7,4, 15, 9]
position_to_delete = 3
#create a linked list
head = SinglyLinkedListNode(elements[0])
current = head
for data in elements[1:]:
    current.next = SinglyLinkedListNode(data)
    current = current.next
#print the original linked list
print("original Linked List")
printLinkedList(head)
#deleting the node at the given position
head = deleteNode(head, position_to_delete)
#print the modified linked list
print("\nLinked List after deletion:")
printLinkedList(head)