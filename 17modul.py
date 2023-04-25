def mysort(array):
    for i in range(len(array)):
        idx_min = i
        for j in range(i, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j
        if i != idx_min:
            array[i], array[idx_min] = array[idx_min], array[i]


def binary_search(array, element, left, right):
    if left > right:
        return False

    if right - left <= 1:
        if array[left] < element <= array[right]:
            return left
        else:
            return False

    middle = (right + left) // 2
    m = array[middle]
    if m >= element:
        return binary_search(array, element, left, middle)
    else:
        return binary_search(array, element, middle, right)



if __name__ == '__main__':
    numbers = list(map(int, input().split()))
    t = int(input("Введите число: "))
    mysort(numbers)
    pos = binary_search(numbers, t, 0, len(numbers) - 1)
    print(numbers)
    if pos is False:
        print(f"Нет чисел меньше {t}")
    else:
        print(pos)