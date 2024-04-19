from datetime import datetime
def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        days_difference = (given_date - today).days
        return days_difference
    except ValueError:
        return "Неправильний формат вхідної дати. Використовуйте формат 'РРРР-ММ-ДД'."

print(get_days_from_today("2024-10-09"))