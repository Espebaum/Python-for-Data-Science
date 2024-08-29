def ft_filter(func, iters):
    res = [item for item in iters if func(item)]
    # should use list comprehensions
    return res


# unittest, filter