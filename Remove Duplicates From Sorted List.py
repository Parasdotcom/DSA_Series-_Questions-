def uniqueSortedList(head):
    # Initialize curr to store head
    curr = head
    
    while head != None and curr.next != None:
        # next element has same value as the current element
        if (curr.next.data == curr.data):
        # Adjust link to remove the next element.
                 curr.next = curr.next.next
        
        else:
            curr = curr.next
    return head