"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next_node=None):
        self.prev = prev
        self.value = value
        self.next = next_node
    
    def delete(self):
        try:
            if self.prev: 
                self.next.prev = self.prev
            if self.next: 
                self.prev.next = self.next
        except: 
            self.next = None
            self.prev = None
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create new_node
        new_node = ListNode(value)
        # 1. add to empty
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
    
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        # update length
        self.length += 1
            
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        removed_value = self.head.value
        self.delete(self.head)
        return removed_value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create new_node
        new_node = ListNode(value)
        # 1. add to empty
        if self.tail is None: 
            self.head = new_node
            self.tail = new_node
        # 2. add to non-empty
        else:
            new_node.prev = self.tail
            new_node.prev.next = new_node
            self.tail = new_node

        # update length
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        removed_value = self.tail.value
        self.delete(self.tail)
        return removed_value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head: 
            return
        self.delete(node)
        self.add_to_head(node.value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail: 
            return
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head is None: 
            return None
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head: #List has 2+ nodes
            self.head = node.next
            node.delete() #updating previous and next pointers
        elif node is self.tail: 
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        node_values = []
        cur_node = self.head
        while cur_node is not None: 
            node_values.append(cur_node.value)
            cur_node = cur_node.next
        return max(node_values)