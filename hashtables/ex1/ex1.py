def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Comments will follow the weights = [4, 6, 10, 15, 16], length = 5, limit = 21 example

    cache = {}

    #length = 5
    for i in range(length):
        #limit = 21. target should be 17, 15, 11, 6, 5 when i = 0, 1, 2, 3, 4
        target = limit - weights[i]
        if target in cache:
            # first target this should find is 6. See comments in else section
            x = cache[target] # x = 1
            pairing = [i, x] # pairing = [3, 1]
            # due to subtraction, there's no way to know which if i had been the larger or smaller index, so sort largest to smallest
            pairing.sort(reverse = True)

            return pairing
        else:
            # targets of 17, 15, 11 would not be found in cache
            # since the output needs the position of the values, store the position (i) to the cache
            # when target is 15, i = 1, and weights[i] = 6, so cache[6] = 1
            cache[weights[i]] = i

    return None
