import unittest
from tkinter import Tk

from fproject.sort import sort_numbers


class TestSortingProgram(unittest.TestCase):
    """Класс для тестирования программы сортировки последовательности чисел"""

    def test_sort_sequence(self):
        """Тестирование функции сортировки последовательности чисел"""
        test_cases = {
            "1, 3, 2, 5, 4": ("По возрастанию", "1, 2, 3, 4, 5"),
            "9, 7, 8, 5, 6": ("По убыванию", "9, 8, 7, 6, 5"),
            "a, b, c": (
                "По возрастанию",
                "Ошибка: Введите числа, разделенные запятыми",
            ),
            "1, 3, 2, 5, 4": ("Несуществующий тип", "Произошла ошибка: ValueError"),
        }

        for sequence, sort_type_result in test_cases.items():
            sort_type, expected_result = sort_type_result
            with self.subTest(
                sequence=sequence, sort_type=sort_type, expected_result=expected_result
            ):
                output_label = Tk().Label()
                sort_numbers(sequence, sort_type, output_label)
                self.assertEqual(output_label.cget("text"), expected_result)


if __name__ == "__main__":
    unittest.main()
