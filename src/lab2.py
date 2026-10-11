# Лабораторна робота №2. Створення та використання функцій, реалізація рекурсії
# Варіант: 3
# ПІБ: Бігун Іван Олександрович 

import random

# ==========================================
# 1. ГЕНЕРАЦІЯ ДАНИХ (Мінімум 20 елементів)
# ==========================================
def generate_sports_data(num_matches: int) -> list:
    """Генерує список словників зі статистикою футбольних матчів."""
    data = []
    for i in range(1, num_matches + 1):
        match = {
            'match_id': i,
            'goals': random.randint(0, 3),        # Забиті голи (від 0 до 3)
            'assists': random.randint(0, 2),      # Гольові передачі (від 0 до 2)
            'distance_km': random.uniform(8.0, 12.5), # Пробіг за матч у км
            'passes': random.randint(20, 60)      # Кількість передач
        }
        data.append(match)
    return data

# ==========================================
# 2. ЗВИЧАЙНІ ФУНКЦІЇ (Мінімум 2)
# ==========================================
def calculate_total_goals(data: list) -> int:
    """Обчислює загальну кількість забитих голів за всі матчі."""
    total = 0
    for match in data:
        total += match['goals']
    return total

def calculate_total_assists(data: list) -> int:
    """Обчислює загальну кількість гольових передач за всі матчі."""
    total = 0
    for match in data:
        total += match['assists']
    return total

# ==========================================
# 3. ФУНКЦІЯ З ПАРАМЕТРАМИ ЗА ЗАМОВЧУВАННЯМ
# ==========================================
def calculate_average_distance(data: list, round_digits: int = 2) -> float:
    """
    Обчислює середню дистанцію, яку пробіг гравець.
    Параметр round_digits має значення за замовчуванням 2 (округлення до сотих).
    """
    if not data:
        return 0.0
    
    total_distance = sum(match['distance_km'] for match in data)
    average = total_distance / len(data)
    
    # Округлюємо до заданої кількості знаків після коми
    return round(average, round_digits)

# ==========================================
# 4. ФУНКЦІЯ ЗІ ЗМІННОЮ КІЛЬКІСТЮ АРГУМЕНТІВ (*args)
# ==========================================
def calculate_team_points(*match_results: str) -> int:
    """
    Обчислює очки команди за серію матчів.
    Приймає будь-яку кількість результатів: 'W' (перемога - 3 очки), 
    'D' (нічия - 1 очко), 'L' (поразка - 0 очок).
    """
    points = 0
    for result in match_results:
        if result == 'W':
            points += 3
        elif result == 'D':
            points += 1
    return points

# ==========================================
# 5. ЛЯМБДА-ФУНКЦІЇ (Мінімум 1-2)
# ==========================================
# Лямбда-функція для обчислення системи "гол + пас" для конкретного матчу
calculate_goal_involvements = lambda match: match['goals'] + match['assists']

# ==========================================
# 6. РЕКУРСИВНА ФУНКЦІЯ
# ==========================================
def find_max_passes_recursive(data: list, start: int, end: int) -> int:
    """
    Рекурсивно знаходить максимальну кількість передач за матч у масиві даних.
    Розділяє список навпіл (алгоритм "розділяй і володарюй").
    """
    # Базовий випадок: якщо залишився лише один елемент
    if start == end:
        return data[start]['passes']
    
    # Рекурсивний випадок: ділимо список навпіл
    mid = (start + end) // 2
    left_max = find_max_passes_recursive(data, start, mid)
    right_max = find_max_passes_recursive(data, mid + 1, end)
    
    # Повертаємо найбільше з двох половин
    return max(left_max, right_max)

# ==========================================
# 7. ФУНКЦІЯ ВИЩОГО ПОРЯДКУ ТА FILTER/MAP
# ==========================================
def apply_to_matches(data: list, func: callable) -> list:
    """
    Функція вищого порядку. Приймає список матчів та іншу функцію (func),
    яку застосовує до кожного матчу.
    """
    result = []
    for match in data:
        result.append(func(match))
    return result

# ==========================================
# 8. ГОЛОВНА ІНТЕРАКТИВНА ПРОГРАМА (Меню)
# ==========================================
def main():
    print("=== Вітаємо в системі аналізу спортивної статистики! ===")
    
    # Генеруємо дані для 25 матчів (більше необхідних 20)
    matches_data = generate_sports_data(25)
    
    while True:
        print("\nОберіть операцію:")
        print("1. Показати всі дані матчів")
        print("2. Загальна статистика (голи та асисти)")
        print("3. Середня дистанція за матч")
        print("4. Знайти рекорд передач за матч (Рекурсія)")
        print("5. Матчі з високою активністю (>11 км) (Використання filter)")
        print("6. Підрахувати очки команди (Тест *args)")
        print("7. Вийти")

        try:
            # Валідація вводу: намагаємось перетворити ввід на ціле число
            choice = int(input("\nВаш вибір (1-7): "))
            
            if choice == 1:
                print("\n--- Дані всіх матчів ---")
                for m in matches_data:
                    print(f"Матч {m['match_id']}: Голи={m['goals']}, Асисти={m['assists']}, Дистанція={m['distance_km']:.1f}км, Передачі={m['passes']}")
            
            elif choice == 2:
                # Використання звичайних функцій
                goals = calculate_total_goals(matches_data)
                assists = calculate_total_assists(matches_data)
                print(f"\nЗагалом забито голів: {goals}")
                print(f"Загалом гольових передач: {assists}")
                print(f"Система гол+пас: {goals + assists}")
                
            elif choice == 3:
                # Використання функції з параметром за замовчуванням
                avg_dist = calculate_average_distance(matches_data) # round_digits = 2 за замовчуванням
                print(f"\nСередня пробіжка гравця за матч: {avg_dist} км")
                
            elif choice == 4:
                # Використання рекурсивної функції
                max_passes = find_max_passes_recursive(matches_data, 0, len(matches_data) - 1)
                print(f"\nРекорд передач за один матч (знайдено рекурсивно): {max_passes}")
                
            elif choice == 5:
                # Використання вбудованої функції filter та lambda
                print("\n--- Матчі, де гравець пробіг більше 11 км ---")
                hard_matches = list(filter(lambda m: m['distance_km'] > 11.0, matches_data))
                for m in hard_matches:
                    print(f"Матч {m['match_id']}: {m['distance_km']:.2f} км")
                    
            elif choice == 6:
                # Демонстрація функції зі змінною кількістю аргументів (*args)
                print("\nПрипустимо, команда зіграла 5 матчів з результатами: Перемога, Нічия, Перемога, Поразка, Перемога")
                points = calculate_team_points('W', 'D', 'W', 'L', 'W')
                print(f"Зароблено очок команди: {points}")
                
            elif choice == 7:
                print("\nДякуємо за використання програми аналізу! До побачення.")
                break
                
            else:
                print("\nПомилка: Невірний вибір. Будь ласка, введіть число від 1 до 7.")
                
        # Обробка помилок (якщо користувач ввів літеру замість числа)
        except ValueError:
            print("\nПомилка: Будь ласка, введіть коректне число.")

# Точка входу в програму
if __name__ == "__main__":
    main()
