def greedy_algorithm(items, budget):
    
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_calories = 0
    selected_items = []
    
    for item, info in sorted_items:
        if budget >= info['cost']:
            selected_items.append(item)
            budget -= info['cost']
            total_calories += info['calories']
    
    return selected_items, total_calories


def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    item_list = list(items.items())
    
    for i in range(1, n + 1):
        name, info = item_list[i - 1]
        cost, calories = info['cost'], info['calories']
        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i-1][b], dp[i-1][b-cost] + calories)
            else:
                dp[i][b] = dp[i-1][b]
    
    # Визначаємо обрані страви
    selected_items = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i-1][b]:
            name = item_list[i-1][0]
            selected_items.append(name)
            b -= items[name]['cost']
    
    selected_items.reverse()
    return selected_items, dp[n][budget]


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

selected_items, total_calories = greedy_algorithm(items, budget)
print(f"Жадібний алгоритм: обрані страви {selected_items}, загальна калорійність: {total_calories}")


selected_items, total_calories = dynamic_programming(items, budget)
print(f"Динамічне програмування: обрані страви {selected_items}, загальна калорійність: {total_calories}")
