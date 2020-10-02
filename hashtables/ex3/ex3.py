def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # [
    #     [1, 2, 3, 4, 5],
    #     [12, 7, 2, 9, 1],
    #     [99, 2, 7, 1,]
    # ]
    # returned output: [1, 2]
    # The above nested list is from the README

    cache = {}
    result = []

    for nestedlist in arrays:
        # first iteration focuses on [1, 2, 3, 4, 5]
        for item in nestedlist:
            # first item is 1
            if item in cache:
                # Increment the existing count
                cache[item] += 1
            else:
                # Start the count for each value in the entire arrays
                cache[item] = 1

            # Now I want to see which items have a count total matching the number of nested lists (in above case: 3)
            if cache[item] == len(arrays):
                result.append(item)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
