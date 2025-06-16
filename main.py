import heapq

# Завдання 1: Мінімізація витрат на з'єднання кабелів
def min_cost_connect_cables(cables):
    if not cables:
        return 0
    
    # Створюємо мінімальну купу з довжин кабелів
    heapq.heapify(cables)
    total_cost = 0
    
    # Поки в купі є принаймні два кабелі
    while len(cables) > 1:
        # Витягуємо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Обчислюємо витрати на їхнє з'єднання
        current_cost = first + second
        total_cost += current_cost
        
        # Додаємо новий кабель назад до купи
        heapq.heappush(cables, current_cost)
    
    return total_cost

# Завдання 2: Об'єднання k відсортованих списків
def merge_k_lists(lists):
    # Видаляємо порожні списки
    lists = [lst for lst in lists if lst]
    if not lists:
        return []
    
    result = []
    # Створюємо мінімальну купу для відстеження найменших елементів
    heap = []
    
    # Додаємо перший елемент з кожного списку до купи разом з індексом списку та позицією
    for i, lst in enumerate(lists):
        heapq.heappush(heap, (lst[0], i, 0))
    
    # Поки купа не порожня
    while heap:
        val, list_idx, element_idx = heapq.heappop(heap)
        result.append(val)
        
        # Якщо в списку є наступний елемент, додаємо його до купи
        if element_idx + 1 < len(lists[list_idx]):
            next_element_idx = element_idx + 1
            heapq.heappush(heap, (lists[list_idx][next_element_idx], list_idx, next_element_idx))
    
    return result

# Приклад використання
if __name__ == "__main__":
    # Тестування Завдання 1
    cables = [4, 3, 2, 6]
    print("Завдання 1: Мінімальні витрати на з'єднання кабелів:", min_cost_connect_cables(cables))  # Очікуваний результат: 29
    # Пояснення: (2+3)=5, (5+4)=9, (9+6)=15 => 5+9+15=29
    
    # Тестування Завдання 2
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    print("Завдання 2: Відсортований список:", merge_k_lists(lists))  # Очікуваний результат: [1, 1, 2, 3, 4, 4, 5, 6]