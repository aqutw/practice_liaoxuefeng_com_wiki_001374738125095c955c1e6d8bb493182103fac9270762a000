def calc0(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc0([1, 2, 3])
print calc0([1, 2, 3, 7])


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc(1, 2)
print calc()

L = [1,2,3]
print calc(L[0], L[1], L[2])
print calc(*L)




def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

person('Adam', 45, gender='M', job='Engineer')

o = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=o['city'], job=o['job'])
person('Jack', 24, **o)






