import heapq

def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)
    total_cost = 0
    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        cost = first + second
        total_cost += cost
        heapq.heappush(cables, cost)
    return total_cost

def merge_k_lists(lists):
    heap = []
    result = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    while heap:
        val, list_idx, element_idx = heapq.heappop(heap)
        result.append(val)
        if element_idx + 1 < len(lists[list_idx]):
            heapq.heappush(heap, (lists[list_idx][element_idx + 1], list_idx, element_idx + 1))
    return result

cables = [4, 3, 2, 6]
result = min_cost_to_connect_cables(cables)
print("Мінімальні загальні витрати на з'єднання кабелів:", result)

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
