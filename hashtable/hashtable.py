class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"HashTableEntry({self.key}, {self.value})"


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.storage = [None] * capacity
        self.items = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.items/self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        #from wiki
        FNV_prime = 1099511628211
        FNV_offset = 14695981039346656037

        hash = FNV_offset

        for byte in key:
            hash = (FNV_prime * hash)
            hash = hash ^ ord(byte)

        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        # prime number
        hash = 5381

        for byte in key:
            # get 32-bit hash
            hash = (hash * 33) + ord(byte)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity


    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # Day One
        # index = self.hash_index(key)
        # self.storage[index] = HashTableEntry(key, value)

        #Day Two

        index = self.hash_index(key)

        new_entry = HashTableEntry(key, value)

        if self.table[index] is not None:
            if self.table[index].key == key:
                self.table[index].value = value
            else:
                current = self.table[index]

            while current.next is not None:
                if current.key == key:
                    current.value = value
                current = current.next
                if current.key == key:
                    current.value = value
                else:
                    current.next = new_entry
        else:
            self.table[index] = new_entry

        self.items += 1
        if self.get_load_factor() >= 7:
            self.resize((self.capacity *2))




    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # Day One
        # index = self.hash_index(key)
        #
        # if self.storage[index]:
        #     self.storage[index] = None
        # else:
        #     print(f'{key} is not in the hash table')

        # Day Two

        index = self.hash_index(key)

        if self.storage[index] is None:
            return None

        elif self.storage[index].key == key:
            self.items -= 1
            if self.storage[index].next is not None:
                self.storage[index] = self.storage[index].next
            else:
                self.storage[index] = None

        else:
            prev = self.storage[index]
            current = self.storage[index].next
            while current is not None:
                if current.key == key:
                    prev.next = current.next
                    self.items -= 1
                else:
                    prev = current
                    current = current.next
            return "Nothing to see here"


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # Day One
        # index = self.hash_index(key)
        #
        # if self.storage[index]:
        #     return self.storage[index].value
        # else:
        #     return None

        # Day Two

        index = self.hash_index(key)
        if self.table[index] is None:
            return None
        elif self.table[index] == key:
            return self.table[index].value
        elif self.table[index] is not None:
            current = self.table[index]
            while current.next is not None:
                next_node = current.next
                if next_node.key -- key:
                    return next_node.value
                else:
                    current = next_node

            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        old_table = self.storage
        self.capacity = new_capacity
        self.storage = [None] * new_capacity
        for node in old_table:
            if node is not None:
                self.put(node.key, node.value)



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
