class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

def removeLoop(head :Node) -> Node:
    # We reached the end of the list and haven't  found any cycle.
    if head == None or head.next == None:
        return None
    # slow pointer this will incremented by 1 nodes.
    slow = head
    # fast pointer this will incremented by 2 nodes.
    fast = head
    
    while True:
        if fast == None or fast.next == None:
            return head
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
        # Cycle found
        fast = head
        
        # starting will point starting node of cycle
        start = None
        
        while fast != slow:
            fast = fast.next
        start = slow
        
        # Finding the previous node of start
        cur = head
        
        while True:
            if cur.next == start:
                cur.next = None
                return head
            cur = cur.next