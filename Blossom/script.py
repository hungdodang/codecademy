from linked_list import Node, LinkedList
from blossom_lib import flower_definitions
class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(self.array_size)]

  def hash(self, key):
    encoded_key = key.encode()
    hash_code = 0
    for x in encoded_key:
        hash_code += ord(x)
    return hash_code
  def compress(self, hash_code):
    return hash_code % self.array_size
  def assign(self, key, value):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)

    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for item in list_at_array:
      if key == item[0]:
        item[1] = value
        return
    list_at_array.insert(payload)

  def retrieve(self, key):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    list_at_index = self.array[array_index]
    for item in list_at_index:
      if key == item[0]:
        return item[1]
    return None
    
blossom = HashMap(len(flower_definitions))
for item in flower_definitions:
    blossom.assign(item[0], item[1])
print(blossom.retrieve('daisy'))

