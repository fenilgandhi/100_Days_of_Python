# Given a iterable xs and a value ys, add value to end of iterable
def append(xs, ys):
    return xs.__add__(ys)


# Given atleast 2 iterables merge their values into a single iterable
def concat(lists):
    def concat_iter():
        for ls in lists:
            for item in ls:
                yield item
    return list(concat_iter())


# Filters a list xs over a function and return only passing values
def filter_clone(function, xs):
    return [i for i in xs if function(i)]


# Return length of given iterable
def length(xs):
    return xs.__len__()


# Run a function on every value of given iterable xs
def map_clone(function, xs):
    return [function(i) for i in xs]


def reverse(xs):
    return xs[::-1]
