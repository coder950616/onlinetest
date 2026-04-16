# Review 1
def add_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

# Problem: 
# my_list is a default variable, it will be initialized at the first call.
# but list is a mutable object, once it is initialized and changed, 
# the next call will not get a empty list.
# for example:
# add_to_list(1) -> [1]
# add_to_list(2) -> [1, 2]

# Correct version
def add_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list



# Review 2
def format_greeting(name, age):
    return "Hello, my name is {name} and I am {age} years old."

# Problem:
# if want to format the string, need to use f-string
# Correct version
def format_greeting(name, age):
    return f"Hello, my name is {name} and I am {age} years old."



# Review 3
class Counter:
    count = 0
    def __init__(self):
        self.count += 1
    def get_count(self):
        return self.count
    
# Problem:
# count is class variable but self.count is instance variable.
# I this this is used to count how many instance is created, so need to use class variable
# Correct version
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
    def get_count(self):
        return Counter.count
 
# Review 4
import threading
class SafeCounter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
 
def worker(counter):
    for _ in range(1000):
        counter.increment()
 
counter = SafeCounter()
threads = []
for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()
    threads.append(t)
 
for t in threads:
    t.join()
 
 # Problem
 # += 1 is operation is not thread safe. we need to add a lock to protect the thread safe.

import threading
class SafeCounter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()
    def increment(self):
        with self.lock:
            self.count += 1
 
def worker(counter):
    for _ in range(1000):
        counter.increment()
 
counter = SafeCounter()
threads = []
for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()
    threads.append(t)
 
for t in threads:
    t.join()

# Review 5
def count_occurrences(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] =+ 1
        else:
            counts[item] = 1
    return counts

# Problem: 
# 1. syntax error. should be += instead of =+
# 2. we need to check the type of the items of lst, if it is mutable type, cannot be a key of dict

# Correct version
def count_occurrences(lst):
    counts = {}
    for item in lst:
        if isinstance(item, (list, dict, set)):
            continue
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

