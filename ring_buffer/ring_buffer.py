from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.count = 0

    def append(self, item):
        # we check if the length of our LL has reached capacity
        if self.storage.length is self.capacity:
            # if it is we need to remove from head
            self.storage.remove_from_head()
        # if it is not, we add to the tail the new entry
        self.storage.add_to_tail(item)
        # and as long as our count it's greater than 0 AND the remainder of capacity is 0..
        if self.count > 0 and self.count % self.capacity == 0:
            # we set our current entry to be our LL tail
            self.current = self.storage.tail
        # keeps a track of how many times we've appended to our LL 
        self.count += 1

        # # LINKED LIST PRINT STATEMENTS
        # print('our linked list', self.storage)
        # print('current', self.current)
        # print('count', self.count)
        # print('our linked list tail', self.current)
        # # RB PRINT STATEMENTS-----------------------
        # print('linked list length', self.storage.length)
        # print('in our RB, whos our head?', head_node.value)
        # print('bf list', list_buffer_contents)
        # print('in our RB, whos our tail?', self.storage.tail.value)

        # OUR LINKED LIST!
         # head            tail
          # v               v
        # [None,'b','c','d','e']

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # checks if current node has any value
        if self.current:
            # if it is, we add the value to the list
            list_buffer_contents.append(self.current.value)
            # we check while current node has a value..
            while self.current.next:
                # current node will now be equal to the current's next node
                self.current = self.current.next
                # we add the current's node value to our list
                list_buffer_contents.append(self.current.value)
        # checks if the ring's length is less than our LL's length
        if len(list_buffer_contents) < self.storage.length:
            # We grab our LL node that is currently the head in a variable
            head_node = self.storage.head
            # and we add the value of it in our ring buffer's list
            list_buffer_contents.append(head_node.value)
            # as long as the length of our RB is less than our Linked List length
            while len(list_buffer_contents) < self.storage.length:
                # we assign the head's next node to be the head
                head_node = head_node.next
                # and we append the value of it to our ring buffer 
                list_buffer_contents.append(head_node.value)
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass


# if __name__ == '__main__':
#     rb = RingBuffer(5)
#     rb.append('a')
#     rb.append('b')
#     rb.append('c')
#     rb.append('d')
#     rb.append('e')
#     rb.append('f')
#     rb.append('g')
#     rb.append('h')
#     rb.append('i')
#     print('GET', rb.get())
