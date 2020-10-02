#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # tickets = [
    #     Ticket{ source: "III", destination: "OOO" },
    #     Ticket{ source: "AAA", destination: "NONE" },
    #     Ticket{ source: "NONE", destination: "III" },
    #     Ticket{ source: "OOO", destination: "AAA" }
    # ]
    # the above array is for visualization. Goal is to return ["III", "OOO", "AAA"]. Notice the "NONE"s are removed
    # Just double-checked the tests. The README removed both "NONE"s, but the tests expects the destination "NONE" to remain

    cache = {}
    route = []

    for i in tickets:
        cache[i.source] = i.destination
        # We should have cache["NONE"] = "III", cache["III"] = "OOO", cache["OOO"] = "AAA", cache["AAA"] = "NONE"

    airport = cache["NONE"] # Initialization for the for-loop below
    for j in range(len(tickets)):
        route.append(airport)
        airport = cache[airport]

    return route
