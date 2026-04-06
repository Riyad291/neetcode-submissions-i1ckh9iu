class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # কি (key) থেকে নোড (node) ম্যাপ করবে

        # বাম (LRU) এবং ডান (MRU) এর জন্য ডামি নোড
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # লিস্টের মাঝখান থেকে নোড সরানোর হেল্পার ফাংশন
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # লিস্টের একদম ডানে (সবচেয়ে নতুন হিসেবে) নোড বসানোর হেল্পার ফাংশন
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # যদি কি-টি থাকে, তবে ওটাকে সরিয়ে আবার শেষে (ডানে) বসান
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # পুরনো নোডটি থাকলে সরিয়ে ফেলুন
            self.remove(self.cache[key])
        
        # নতুন নোড তৈরি করে ডিকশনারি ও লিস্টে যোগ করুন
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # যদি ক্যাপাসিটি ছাড়িয়ে যায়
        if len(self.cache) > self.cap:
            # বাম পাশের (সবচেয়ে পুরনো) নোডটি ডিলিট করুন
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]