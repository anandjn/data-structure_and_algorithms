#!/usr/bin/python

'''
Implementing hash tables using predefined hash function.
It has 2 methods(setting and getting).
      TASK                  Time-complexity
adding a new pair                 O(1)
updating and existing pair        O(n)
getting value for key             O(n) 
'''


class HashTable:
  def __init__(self, size):
    self.size = size
    self.data = [[] for _ in range(size)]

  def _hash(self, key):
    #python internal function to create hash
    #modulous (%) will keep the hash in range
    hashValue = hash(key) % self.size
    return hashValue
  
  def seting(self, key, value):
    address = self._hash(key)
    #using the bucket at index = address to perform following action
    bucket = self.data[address]
    append_flag = True
    #1 if the data for the same key exist in bucket@address then update/over-write
    for i in range(len(bucket)):
      if bucket[i][0] == key:
        #update, set append_flag to  False
        self.data[address][i][1] = value
        append_flag = False
        break
    #2 else add/append
    if append_flag:  
      self.data[address].append([key,value])

    #print(self.data)

  def getting(self, key):
    #passing key to hash function to locate its bucket address
    address = self._hash(key)
    bucket = self.data[address]
    #avoiding 0 element bucket
    if len(bucket) == 0:
      print(None)
      return None
    #iterating over bucket and comparing each key
    for k,v in  bucket:
      if key == k:
        print(v)
        return v


#hash table of size 50(buckets)
myHashTable = HashTable(50)
myHashTable.seting("grapes", 10000)
myHashTable.seting("grapes", 2000)
myHashTable.getting('grapess')
myHashTable.seting("apples", 50)
myHashTable.getting('apple')
myHashTable.getting('apples')

