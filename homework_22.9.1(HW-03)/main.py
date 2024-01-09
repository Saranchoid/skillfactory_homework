def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return low


def sort_list(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def main():
    try:
        input_str = input("Введите последовательность чисел через пробел: ")
        numbers = list(map(float, input_str.split()))
        sorted_numbers = sort_list(numbers)
        print(sorted_numbers)

        user_number = float(input("Введите любое число: "))

        position = binary_search(sorted_numbers, user_number)
        if position == len(sorted_numbers):
            print("Указанное число больше всех чисел в последовательности.")
        else:
            print(f"Позиция элемента, который меньше введенного числа: {position - 1}")
    except ValueError:
        print("Ошибка: Введены некорректные данные. Пожалуйста, введите числа через пробел.")


if __name__ == "__main__":
    main()
