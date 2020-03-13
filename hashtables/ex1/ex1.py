#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    
    # list `weights` of item weights
    #get_indices_of_item_weights` that finds two items whose sum of weights equals the weight limit `limit`
    """
    YOUR CODE HERE
    """
    # insert items into my hastable
    for i in range(length):
        hash_table_insert(ht,weights[i], i )
    # get each item from hastable
    for i in range(length):

        checked_weight = hash_table_retrieve(ht, (limit-weights[i]))

        if checked_weight:
            if checked_weight > i:
                return [checked_weight, i]
            else:
                return [index, checked_weight]
    return None

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
