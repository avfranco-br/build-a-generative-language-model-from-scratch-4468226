import random
from collections import defaultdict

tokens = ["I", "try", "to", "learn", "something", "new", "every", "day"]

graph = defaultdict(list)
graph["word"].append("hi")

print(graph["word"])

for index, token in enumerate(tokens):
    print(index,token)

print(random.choice(tokens))
print(random.choice(tokens))
print(random.choice(tokens))
