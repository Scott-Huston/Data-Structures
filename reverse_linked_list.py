from doubly_linked_list import DoublyLinkedList as DLL

dll = DLL()

# initializing list
for i in range(10):
    dll.add_to_tail(i)

# def reverse_list
node = dll.head
prev = None

while node:
    next = node.next
    node.prev = node.next
    node.next = prev
    prev = node
    node = next

temp_head = dll.head
dll.head = dll.tail
dll.tail = temp_head

# print list
node = dll.head
while node:
    print(node.value)
    node = node.next

def reverse_list(dll):
    node = dll.head
    prev = None
    
    # looping through list and reversing connections
    while node:
        next = node.next
        node.prev = node.next
        node.next = prev
        prev = node
        node = next

    # changing head and tail of linked list so the list starts at
    # what was previously the end node
    temp_head = dll.head
    dll.head = dll.tail
    dll.tail = temp_head

    return dll
    