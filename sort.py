import time
import tkinter as tk
from tkinter import ttk


def sort_numbers():
    """
    Функция для сортировки последовательности чисел и вывода результата в графический интерфейс.

    Проверяет ввод пользователя, сортирует введенные числа в соответствии с выбранным типом сортировки
    и выводит результат в текстовое поле с указанием времени, затраченного на сортировку.

    """
    input_text = entry.get()
    sort_type = combo.get()

    # Проверка на пустой ввод
    if not input_text:
        result_label.config(text="Введите последовательность чисел")
        return

    try:
        # Парсинг введенной последовательности чисел и проверка на целые и положительные числа
        numbers = [int(x) for x in input_text.split(",") if int(x) > 0]

        # Проверка на пустой список после фильтрации
        if not numbers:
            result_label.config(
                text="Введите корректную последовательность целых положительных чисел"
            )
            return

        # Сортировка в соответствии с выбранным типом
        if sort_type == "По возрастанию":
            start_time = time.time()
            numbers.sort()
            end_time = time.time()
            sorted_numbers = numbers
        elif sort_type == "По убыванию":
            start_time = time.time()
            numbers.sort(reverse=True)
            end_time = time.time()
            sorted_numbers = numbers
        result_label.config(
            text=f"Отсортированная последовательность: {sorted_numbers}\n"
            f"Время сортировки: {end_time - start_time} сек."
        )
    except ValueError:
        result_label.config(
            text="Введите корректную последовательность целых положительных чисел"
        )


# Создание графического интерфейса
root = tk.Tk()
root.title("Программа сортировки чисел")

# Поле ввода
entry = tk.Entry(root)
entry.pack()

# Раскрывающийся список
sort_options = ["По возрастанию", "По убыванию"]
combo = ttk.Combobox(root, values=sort_options)
combo.pack()

# Кнопка "Start"
start_button = tk.Button(root, text="Start", command=sort_numbers)
start_button.pack()

# Поле вывода надписи
result_label = tk.Label(root, text="")
result_label.pack()

# Запуск графического интерфейса
root.mainloop()
