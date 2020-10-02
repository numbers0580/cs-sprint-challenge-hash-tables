# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # paths = [
    #     "/usr/local/share/foo.txt",
    #     "/usr/bin/ls",
    #     "/home/davidlightman/foo.txt",
    #     "/bin/su"
    # ]
    # queries = [
    #     "ls",
    #     "foo.txt",
    #     "nosuchfile.txt"
    # ]
    # output: [ "/usr/local/share/foo.txt", "/usr/bin/ls", "/home/davidlightman/foo.txt" ]

    # So thinking in terms of Venn Diagrams, the output would be the intersection of paths and queries
    # Effectively, not every path will be in the result, and not every query would be in the result

    # Note: README has a list of "paths", but tests have a list of "files" which are passed in as a parameter to this function

    cache = {}
    result = []

    for item in files:
        eachitem = item.split("/")

        val = eachitem[len(eachitem) - 1]
        if val not in cache:
            # cache["foo.txt"] = "/usr/local/share/foo.txt"
            cache[val] = []
            cache[val].append(item)
        else:
            # cache["foo.txt"] = ["/usr/local/share/foo.txt", "/home/davidlightman/foo.txt"]
            cache[val].append(item)

    for item in queries:
        if item in cache:
            # Found it!
            # In the comments in above for-loop, there may be cases where cache[item] is a list of multiple strings. Use extend instead of append here
            result.extend(cache[item])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
