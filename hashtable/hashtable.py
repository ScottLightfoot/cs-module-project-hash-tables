class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
# MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity = 8):
        self.capacity = capacity
        self.table = [None] * capacity
        self.stored_nodes = 0
        # Your code here


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.stored_nodes / self.capacity


    def fnv1(self, key, seed=0):
        """
        FNV-1 Hash, 64-bit
        """
        # 64bit
        FNV_prime = 2**40 + 2**8 + 0xb3
        FNV_offset = 14695981039346656037

        hash = FNV_offset + seed
        for c in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(c)
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for i in key:
            hash = (( hash << 5) + hash) + ord(i)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity


    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        idx = self.hash_index(key)
        if self.table[idx] == None:
            new_entry = HashTableEntry(key, value)
            self.table[idx] = new_entry
            self.stored_nodes += 1
        elif self.table[idx].key == key:
            self.table[idx].value = value
        elif self.table[idx].next == None:
            self.table[idx].next = HashTableEntry(key, value)
            self.stored_nodes += 1
        else:
            curr = self.table[idx]
            while curr.key != key:
                if curr.next.key == key:
                    curr.next.value = value
                elif curr.next == None:
                    curr.next = HashTableEntry(key, value)
                curr = curr.next
        if self.get_load_factor() > .7:
            self.resize(self.capacity*2)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        idx = self.hash_index(key)
        # # Assign None to key pair value ---
        # if self.get(key) == None:
        #     print(f'key "{key}" not found in table')
        # else:
        #     self.put(key, None)

        # # True delete ---
        node = self.table[idx]
        if node.key == key and node.next != None:
            self.table[idx] = node.next
            del(node)
            self.stored_nodes -= 1
        elif node.key == key:
            del(node)
            self.stored_nodes -= 1
            self.table[idx] = None
        else:
            nxt = node.next
            while nxt.next != None:
                if nxt.key == key:
                    node.next = nxt.next
                    del(nxt)
                    self.stored_nodes -= 1
                node = nxt
                nxt = node.next
            if nxt.key == key:
                node.next = nxt.next
                del(nxt)
                self.stored -= 1
        if self.get_load_factor() < .2:
            self.resize(self.capacity/2)


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        idx = self.hash_index(key)
        entry = self.table[idx]
        if entry == None:
            return None
        while entry.key != key:
            if entry.next == None:
                return None
            else:
                entry = entry.next
        return entry.value


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        new_capacity = max([8, new_capacity])
        nodes = [i for i in self.table if i != None]
        self.table = [None] * new_capacity
        self.capacity = new_capacity
        for node in nodes:
            while node != None:
                self.put(node.key, node.value)
                node = node.next


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
