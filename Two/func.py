def doubler(f):
    def g(x):
        return 2 * f(x)

    return g


def f1(x, y):
    return x + y


a = doubler(f1)

# print(a(3, 1))


def magic(*args, **kwargs):
    print('unnamed args:', args)
    print('keyword args:', kwargs)


magic(1, 2, key='word', key2='word2')


def other_way_magic(x, y, z):
    return x + y + z


x_y_list = [1, 2]
z_dict = {'z': 3}
print(other_way_magic(*x_y_list, **z_dict))


def doubler_correct(f):
    """works no matter what kind of inputs f expects"""
    def g(*args, **kwargs):
        """whatever arguments g is supplied pass them through to f"""
        return 2 * f(*args, **kwargs)
    return g


g = doubler_correct(f1)
print(g(1, 3))
