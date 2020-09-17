"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_value(self):
        return self.value
    def get_next_node(self):
        return self.next
    def set_next_node(self, new_next):
        self.next_node = new_next
                
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
        temp = self.head
        count = 0
        while(temp):
            count += 1
            temp = temp.get_next_node()
        self.length = count
        return self.length

    def get_prev_node(self, node):
        if self.head == None or self.head == self.tail:
            return None
        else: 
            cur_node = self.head
            while cur_node is not None:
                if cur_node.get_next_node() == node:
                    return cur_node
                else:
                    cur_node = cur_node.get_next_node()
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if self.head == None: 
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        elif self.head == self.tail: 
            new_node = ListNode(value, None, self.head)
            self.head = new_node
            self.tail = self.head 
        else: 
            new_node = ListNode(value, None, self.head)
            self.head = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head == None: 
            return None
        else:
            ret_value = self.head.get_value()
            if self.head == self.tail: 
                self.head = None
                self.tail = None
                return ret_value
            else:
                self.head = self.head.get_next_node()
                return ret_value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.head == None: 
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        elif self.head == self.tail: 
            new_node = ListNode(value, self.tail, None)
            self.tail = new_node
            self.head = self.tail 
        else:
            new_node = ListNode(value, self.tail, None)
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail == None: 
            return None
        else:
            ret_value = self.tail.get_value()
            if self.head == self.tail: 
                self.head = None
                self.tail = None
                return ret_value
            else:
                self.tail = self.get_prev_node(self.tail)
                return ret_value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head == None: 
            return None
        elif self.head == self.tail: 
            return self.head.get_value()
        else:
            cur_node = self.head
            next_node = cur_node.get_next_node()
            while cur_node is not None: 
                if cur_node.get_value() < next_node.get_value():
                    cur_node = next_node 
                else: 
                    return cur_node.get_value()