#!usr/bin/env python3

''' Author: Matomo Nakamura
    File: priority_queue.py
    Purpose: get minimum number from key as a prioryty number,
        it gets value by using priority number.
'''

class PriorityQueue_Terrible:
    # Constructor
    def __init__(self):
        self._key = []
        self._val = []

    # Adds an item to the priority queue
    def add(self, key,val):
        self._key.append(key)
        self._val.append(val)
        self._val.sort()
        self._key.sort()

    # Return a string of contents of queue
    def __str__(self):
        string = ""
        for key in range(len(self._key)):
            string += str(self._key[key]) + ": " + str(self._val[key]) + ", "
        string = "{" + string[:-2] + "}"
        return string

    # Return the number of items in queue
    def __len__(self):
        return len(self._key)

    # Return True id the queue contains no pairs
    def is_empty(self):
        return not bool(self._key)

    # Return all of the keys in queue
    def keys(self):
        return self._key

    # Return all of the values in queue
    def values(self):
        return self._val

    # Peek at the first item in the queue
    def peek_min_key(self):
        assert self.is_empty()==False
        mini = min(self._key)
        return mini


    def peek_min_val(self):
        assert self.is_empty()==False
        mini = min(self._val)
        return mini

    # Remove the item with lowest key and return the value
    def get_min(self):
        assert self.is_empty()==False
        mini = min(self._key)
        index = self._key.index(mini)
        self._key.remove(mini)
        print(self._key)
        print(self._val)
        return self._val[index]


def main():
    print("Creating two empty queues...")
    q1 = PriorityQueue_Terrible()
    q2 = PriorityQueue_Terrible()
    q3 = PriorityQueue_Terrible()

    print("Adding four keys to q1 (in order)...")
    q1.add(-100, 1025)
    q1.add(  0 , None)
    q1.add(1024, "")
    q1.add(1025, [-100,0,1024,1025])
    print()

    print("Adding four keys to q2 (in reverse order)...")
    q2.add(1025, [-100,0,1024,1025])
    q2.add(1024, "")
    q2.add(  0 , None)
    q2.add(-100, 1025)
    print()

    print("Adding four keys to q3 (in shuffled order)...")
    q3.add(-100, 1025)
    q3.add(1025, [-100,0,1024,1025])
    q3.add(1024, "")
    q3.add(  0 , None)
    print()



    print("Testing the various query properties (q1)...")
    print("len:          ", len(q1))
    print("is_empty:     ", q1.is_empty())
    print("keys (first): ", sorted(q1.keys())[0])
    print("keys (sorted):", sorted(q1.keys()))
    print("__str__:      ", str(q1))
    print()

    print("Testing the various query properties (q2)...")
    print("len:          ", len(q2))
    print("is_empty:     ", q2.is_empty())
    print("keys (first): ", sorted(q2.keys())[0])
    print("keys (sorted):", sorted(q2.keys()))
    print("__str__:      ", str(q2))
    print()

    print("Testing the various query properties (q3)...")
    print("len:          ", len(q3))
    print("is_empty:     ", q3.is_empty())
    print("keys (first): ", sorted(q3.keys())[0])
    print("keys (sorted):", sorted(q3.keys()))
    print("__str__:      ", str(q3))
    print()



    print("Removing one element from each queue:")
    print("  q1:", q1.get_min())
    print("  q2:", q2.get_min())
    print("  q3:", q3.get_min())
    print()

    print("Removing one element from each queue:")
    print("  q1:", q1.get_min())
    print("  q2:", q2.get_min())
    print("  q3:", q3.get_min())
    print()

    print("Removing one element from each queue:")
    print("  q1:", q1.get_min())
    print("  q2:", q2.get_min())
    print("  q3:", q3.get_min())
    print()

    print("Removing one element from each queue:")
    print("  q1:", q1.get_min())
    print("  q2:", q2.get_min())
    print("  q3:", q3.get_min())
    print()



    print("Testing the various query properties (q1)...")
    print("len:          ", len(q1))
    print("is_empty:     ", q1.is_empty())
    print("keys (sorted):", sorted(q1.keys()))
    print("__str__:      ", str(q1))
    print()

    print("Testing the various query properties (q2)...")
    print("len:          ", len(q2))
    print("is_empty:     ", q2.is_empty())
    print("keys (sorted):", sorted(q2.keys()))
    print("__str__:      ", str(q2))
    print()

    print("Testing the various query properties (q3)...")
    print("len:          ", len(q3))
    print("is_empty:     ", q3.is_empty())
    print("keys (sorted):", sorted(q3.keys()))
    print("__str__:      ", str(q3))
    print()



    print("Testcase completed successfully.")
main()