class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node
  
  def __repr__(self):
    return f'{self.value} {self.next_node}'

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def __repr__(self):
    return f'{self.head}'

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    #TO BE COMPLETED 
    # We set a variable initialized to None, because the previous the head of the LL is None
    prev = None
    # while the head of our LL exists
    while self.head:
      # we grab a copy of our the LL current head
      temp = self.head
      # we reassign the head of our LL to be the next node in the LL
      self.head = self.head.next_node
      # the pointer of temp (our previous head) will point to prev
      temp.next_node = prev
      # we set the previous now to be our previous head (temp)
      prev = temp
    # if the head equals None, it means we have reached the end of our LL
    # and we set the head to be equal to the prev (our last node) 
    self.head = prev

# ***IMPORTANT***
# WE DONT CHANGE THE VALUE OF OUR NODES AS WE ITERATE, THE ONLY THING WE CHANGE IS OUR POINTERS!

# input [1 > 2 > 3 > 4 > 5]
# end result [1 < 2 < 3 < 4 < 5]

# if __name__ == '__main__':
#   ll = LinkedList()
#   ll.add_to_head(1)
#   ll.add_to_head(2)
#   ll.add_to_head(10)
#   print(ll)
#   print('head', ll.head)
#   ll.reverse_list()
#   print('head', ll.head)