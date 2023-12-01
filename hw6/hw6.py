data = []


def binary_search(lst, number):
    l = lst[0]
    r = lst[-1]
    m = len(lst) // 2
    while True:
        if m < number:
            data.append(m)
            l = m
            m = (l + r) // 2
        elif m > number:
            data.append(m)
            r = m
            m = (l + m) // 2
        elif m == number:
            data.append(m)
            return "всё!"


print(binary_search(range(1, 51), 12), f"{data} количество попыток - {len(data)}")

sort_lst = []


def bubble_sort(lst):
    while len(lst) != 0:
        m = lst.index(min(lst))
        sort_lst.append(lst.pop(m))
    return f"отсортированный список - {sort_lst}"


print(bubble_sort([111, 54, 44, 14, 62, 112, 32]))
