

# Complete the printLinkedList function below.
#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
def printLinkedList(head):
    
    current = head #Make the variable to read the data
    
    # Looping the head
    while current is not None: #check by loop if the head is none
        print(current.data) #print data of the head
        current = current.next #the loop will read the next node by.next
        

if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)
