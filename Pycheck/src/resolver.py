from libs.perceptron.Pyceptron import load

def get_numbers(sums):
    numbers = []
    for s in sums:
        number = ''
        for d in s.digits:
            number += p.resolve(d)
        number = number[::-1]
        numbers.append(number)
    return reversed(numbers)

p = load('E:\\p3')