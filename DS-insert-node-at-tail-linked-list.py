#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
# 
#
def insertNodeAtTail(head, data):
    
    #define reference of new the new node value
    #SinglyLinkedListNode is default from python
    #(data) is the reference of the new data
    newNode = SinglyLinkedListNode(data)
    
    #This is to define the new data in the head
    if head is None:
        return newNode
    
    #define variable of the current head
    current = head
    
    #kalo misalkan di node selanjutnya itu masih ada value, maka:
    while current.next is not None:
        #berarti ya looping nya lanjut terus
        current = current.next
        #loop terus sampai looping nya menemukan tidak ada value
    
    #Jika ternyata di Node tidak ada value, maka akan di add value yaitu newNode
    current.next = newNode
    
    #kembalikan head
    return head
        
    
        #linkedList gabisa pake index buat nyari value dalemnya
        #
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()
