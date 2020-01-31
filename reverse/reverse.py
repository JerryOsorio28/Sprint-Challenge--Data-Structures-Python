class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

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
    # TO BE COMPLETED
    # first we set a variable that will refer to the previous node, initialized to None
    previous = None
    # while the head node of our linked list is not None
    while self.head is None:
      # we grab the value of our current's next node
      next_node = self.head.next_node
      # we set the head's next node to be our previous 
      self.head.next_node = previous
      # we set that previous now to have the value of the head
      previous = self.head
      # and we change our new head to be our next node
      self.head = next_node
    # when the head of our LL is None, we set the head to be our previous
    self.head = previous