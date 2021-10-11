# this file is used to practice collection module of python
# collections module provides general purpose built-in containers, dict, list, set and tuple
from collections import deque, defaultdict, Counter

# first one: deque: list-like container with fast appends and pops on either end
list_a = [1, 2, 3, 4, 5]
double_queue = deque(list_a)
# popleft() -- > left, pop() -- > right
result_a = double_queue.popleft()
double_queue.append(6)
print(double_queue)

# second one defauldict: defaultdict could use factory functions and if key vaules do not exist
# it will automatically make it up
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
    d[k].add(v)
result = sorted(d.items())
print(result)

# third one: Counter()
list_c = ['a', 'b', 'e']
c = Counter(list_c)
print(list(c))
# c.total new in python 3.10
# print(c.total())
c['f'] += 1
print(c)

# defaultdict with Counter()
feature_label_counts = defaultdict(Counter)
feature_label_counts['e']['T'] += 1
feature_label_counts['e']['F'] += 1
feature_label_counts['e']['T'] += 1
feature_label_counts['f']['T'] += 1
print(feature_label_counts)
print(feature_label_counts['e']['G']) # because not appear, so return 0