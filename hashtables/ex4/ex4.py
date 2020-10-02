def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # input: [ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]
    # Return only the postive numbers that have a corresponding negative number in the list
    # output: [ 1, 3, 4 ]

    cache = {}
    result = []

    for item in a:
        # Make all values positive. Multiple negative values by -1
        val = item
        if val < 0:
            val = val * -1

        if val in cache:
            # Increment existing count
            cache[val] += 1
        else:
            # Start the count for each val at 1
            cache[val] = 1

        # Now check for which vals have a total count of 2 (1 for positive, and 1 for the negative)
        if cache[val] == 2:
            result.append(val)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
