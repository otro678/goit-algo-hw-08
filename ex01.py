import heapq

def min_connection_heap(cables):
    # робимо мінімальну купу зі списук кабелів
    heapq.heapify(cables)
    total_cost = 0
    
    # з'єднуємо два найменших поки є більше 1 елемента
    while len(cables) > 1:
        # берем два найкоротших кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        cost = first + second
        total_cost += cost
        
        # новий кабель назад до купи
        heapq.heappush(cables, cost)
    
    return total_cost

cables = [5, 2, 8, 3, 7, 10, 15, 12]
print(f"Мінімальні витрати на з'єднання: {min_connection_heap(cables)}")