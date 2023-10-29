import os
import numpy
import pickle
from numpy import dot
from numpy.linalg import norm


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

with open(CURRENT_DIR + "/word_to_vector_trsf.pkl", "rb") as pk:
    word_to_vector = pickle.load(pk)

def cosine_similarity(vec_a, vec_b):
    numerator = sum(vec_a[i] * vec_b[i] for i in range(len(vec_a)))
    denominator = (norm(vec_a) * norm(vec_b))

    return numerator / denominator

# Words with higher cosine similarity will come later in the sorted list.
# Should return the top_k closest words to a given word
# Sorted list needs to be reversed - descending order
def similar_words(word="tree", top_k=10):
    return sorted(
        word_to_vector.keys(), 
        key=lambda x: cosine_similarity(word_to_vector[x], word_to_vector[word]),
        reverse=True
    )[:top_k]

result = similar_words("tree", top_k=10)
print(result)

print(cosine_similarity(word_to_vector["mother"], word_to_vector["father"]))