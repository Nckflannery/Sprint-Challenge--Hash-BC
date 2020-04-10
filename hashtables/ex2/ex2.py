#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # Iterate through tickets and add to hash_table with items as (source, destination)
    for i in tickets:
        hash_table_insert(hashtable, i.source, i.destination)
    # First flight source = none and last flight dest. = none
    # So, origin:
    origin = hash_table_retrieve(hashtable, "NONE")
    # Create empty list to hold destinations
    destinations = []
    # Iterate through all items until you hit destination "NONE" (last flight)
    while origin != "NONE":
        destinations.append(origin)
        # Get destination of next flight
        origin = hash_table_retrieve(hashtable, origin)
    return destinations
