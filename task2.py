import random

def get_numbers_ticket(min_num, max_num, quantity):
    if min_num < 1 or max_num > 1000 or quantity > (max_num - min_num + 1):
        print("Числа введені не коректно")
        return []

    numbers_set = set()

    while len(numbers_set) < quantity:
        numbers_set.add(random.randint(min_num, max_num))

    return sorted(list(numbers_set))

lottery_numbers = get_numbers_ticket(10, 14, 6)
print("Ваші лотерейні числа:", lottery_numbers)