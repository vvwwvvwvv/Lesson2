

def get_summ(num_one, num_two):
    try:
        num_one = int(num_one)
        num_one = int(num_two)
    except ValueError:
        return 'Type error'
    return num_two+num_two

print(get_summ(17, 3))
print(get_summ(72, -3))
print(get_summ(6, 17.3))
print(get_summ('w', 3))
print(get_summ(99, '  '))

