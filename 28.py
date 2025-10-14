def generate_cube_numbers(end):
    n = 2
    while True:
        cube = n ** 3
        if cube > end:
            break
        yield cube
        n += 1

from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8]
assert list(generate_cube_numbers(100)) == [8, 27, 64]
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000]
print('Ok')