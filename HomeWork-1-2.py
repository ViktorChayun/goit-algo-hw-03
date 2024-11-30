import random

# LESSONS 2
"""
    функція - генерує набір унікальних випадкових чисел для лотереї
    Параметри функції:
        min - мінімальне можливе число у наборі (не менше 1).
        max - максимальне можливе число у наборі (не більше 1000).
        quantity - кількість чисел, які потрібно вибрати (значення між min і max).
    
    Результат:
        - Функція генерує вказану кількість унікальних чисел у заданому діапазоні.
        - Функція повертає список випадково вибраних, відсортованих чисел. 
        - Числа в наборі не повинні повторюватися (повинні бути унікальні)
        - Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.
"""
def get_numbers_ticket(min, max, quantity):
    # перевірка на коеректність введених папарметрів
    if not quality_check_done(min, max, quantity):
        return []
    
    # генеруємо список можливих номерів в заданому діапазоні
    possible_numbs = []
    for i in range(min, max+1):
        possible_numbs.append(i)
    res = random.sample(possible_numbs, quantity)
    res.sort()
    
    return res

def quality_check_done(min, max, quantity):
    # працюємо лише з цілими числами
    if not isinstance(min, int) or not isinstance(max, int) or not isinstance(quantity, int):
        return False
    
    if min >= 1 and min <= 1000 and min <= max and max <= 1000:
        # к-ть унікальних чисел може бути, якщо це дозволяє діапазон між min і max
        # quantity повинна бути не менше 1 значення
        if quantity>=1 and quantity <= max-min+1:
            return True
    
    return False

# tests for guality_check_done
values_for_check = [
    {"min": 1,"max":"4", "quantity": 100},
    {"min": "1","max":4.0, "quantity": 100},
    {"min": 1,"max":4.0, "quantity": 100},
    {"min": 1,"max":4, "quantity": 100},
    {"min": -1,"max":4, "quantity": 10},
    {"min": 10,"max":4, "quantity": 100},
    {"min": 4,"max":10, "quantity": 100},
    {"min": 4,"max":10, "quantity": 7},
    {"min": 4,"max":10, "quantity": -5},
    {"min": 1,"max":10, "quantity": 11},
    {"min": 1,"max":1001, "quantity": 11},
    {"min": 10,"max":1, "quantity": 1},
    {"min": 10,"max":20, "quantity": 15},
    {"min": 10,"max":10, "quantity": 2},
    {"min": 0,"max":10, "quantity": 5},
    
    {"min": 4,"max":10, "quantity": 2},
    {"min": 10,"max":10, "quantity": 1},
    {"min": 10,"max":20, "quantity": 10},
    {"min": 10,"max":20, "quantity": 5},
    {"min": 1,"max":10, "quantity": 5},
    {"min": 1,"max":49, "quantity": 6},
    {"min": 1,"max":36, "quantity": 5},
]
for val in values_for_check:
    min, max, quantity = val["min"], val["max"], val["quantity"]
    
    quality_check= quality_check_done(min, max, quantity)
    func_res = get_numbers_ticket(min, max, quantity)
    
    print(f"quality_check_done(min={min},max={max}, quantity = {quantity}) = {quality_check}")
    print(f"get_numbers_ticket(min={min},max={max}, quantity = {quantity}) = {func_res}\n")