def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x

print my_abs(-3)
print my_abs('A')


def fn001():
    return

print fn001()

def fn002():
    pass

print fn002()

def fn002a():
    pass
    return

print fn002a()
