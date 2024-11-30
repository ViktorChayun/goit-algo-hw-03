from datetime import datetime, timedelta

# LESSONS 1
# розраховує кількість днів між заданою датою і поточною датою.
# date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09')
# Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. 
# Якщо задана дата пізніша за поточну, результат має бути від'ємним.
# У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
def get_days_from_today(date): 
    try:
        date_obj = datetime.strptime(date,"%Y-%m-%d").date()
        curr = datetime.today().date()
    except ValueError:
        return None
    
    return (curr - date_obj).days

# тестування функції
values = ["2024-11-02", "2024.11-02", "2024.11.02", "2024.12.31", "2024-12-31"]

for val in values:
    print(f"{val} --> {get_days_from_today(val)}")