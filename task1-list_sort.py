class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result) + " -> None"


def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev



def insertion_sort_list(head):
    if not head or not head.next:
        return head

    sorted_head = Node(float('-inf'))
    current = head

    while current:
        prev_node = sorted_head
        while prev_node.next and prev_node.next.data < current.data:
            prev_node = prev_node.next

        next_node = current.next
        current.next = prev_node.next
        prev_node.next = current
        current = next_node

    return sorted_head.next



def merge_sorted_lists(l1, l2):
    dummy = Node()
    tail = dummy

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2

    return dummy.next




# Створення списку
head = Node(4)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(3)

print("Start list:")
print(head)
# Реверсування списку
reversed_list = reverse_list(head)

print("Reversed list:")
print(reversed_list)

# Сортування списку
sorted_list = insertion_sort_list(reversed_list)

print("Sorted list:")
print(sorted_list)

# Створення ще одного списку
head2 = Node(5)
head2.next = Node(6)

# Об'єднання двох відсортованих списків
merged_list = merge_sorted_lists(sorted_list, head2)

print("Merged list:")
print(merged_list)
