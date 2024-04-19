import random


def get_numbers_ticket(min, max, quantity):
    if not 1 <= min <= max <= 1000 or quantity <= 0:
        return []

    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))

    return sorted(list(numbers))


lottery_numbers = get_numbers_ticket(1, 1000, 16)
print("Ваші лотерейні числа:", lottery_numbers)