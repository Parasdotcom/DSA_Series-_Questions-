def removeDuplicates(head):
    p = head
    # Outer loop to pick element.
    while p != None:
        # Initialize the inner loop pointer.
        q = p.next

        # Keep track of previous node.
        prev = p

        while q != None:
            if p.data == q.data:
                # Found a duplicate of node 'p'. Now, we need to remove it.
                # Firstly update the next pointer of the previous node.
                prev.next = q.next

                # Delete the duplicate node.
                del q

                # Move the inner loop pointer to the next node.
                q = prev.next
            else:
                # Node 'q' is not a duplicate. So, move to the next node.
                prev = q
                q = q.next

        # Move the outer loop pointer to the next node.
        p = p.next

    return head
