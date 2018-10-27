_and = 5 & 6

_or = 5 | 6

_xor = 5 ^ 6

_sl = 5 << 2

_sr = 5 >> 2

print(
    '5 & 6 = ',
    '0#{0:b} & 0#{1:b} = 0#{2:b} = '.format(5, 6, _and),
    _and,
    )

print(
    '5 | 6 = ',
    '0#{0:b} | 0#{1:b} = 0#{2:b} = '.format(5, 6, _or),
    _or,
    )

print(
    '5 << 1 = ',
    '0#{0:b} << {1:b} = {2:b} = '.format(5, 2, _sl),
    _sl
)

print(
    '5 >> 1 = ',
    '0#{0:b} >> {1:b} = {2:b} = '.format(5, 2, _sr),
    _sr
)
