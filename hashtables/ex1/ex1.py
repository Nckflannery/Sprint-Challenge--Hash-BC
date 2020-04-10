#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # Number of items in the list
    for i in range(length):
        # Get limit - weight at each index (will be None initially)
        j = hash_table_retrieve(ht, limit-weights[i])
        if j is not None:
            return (i, j)
        else:
        # If it doesn't exist (initialized to None) insert the weight at that spot
            hash_table_insert(ht, weights[i], i)
    # If no items sum = limit, return none
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
