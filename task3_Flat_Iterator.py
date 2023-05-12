class FlatIterator:
    """
    Итератор обрабатывающий списки с любым уровнем вложенности.
    """
    def __init__(self, list_of_list):
        # Конструктор итератора.
        # Принимает список списков и сохраняет его в атрибуте self.list_of_list
        self.list_of_list = list_of_list

    def __iter__(self):
        # Метод, возвращающий сам итератор
        # Создаём список с помощью вспомогательной функции _flatten_list и сохраняем его в self.flat_list
        self.flat_list = self._flatten_list(self.list_of_list)
        # Инициализируем счётчик, который будет указывать на текущий элемент списка
        self.current = 0
        return self

    def __next__(self):
        # Метод, возвращающий следующий элемент итератора
        # Если мы ещё не дошли до конца списка, то возвращаем текущий элемент
        if self.current < len(self.flat_list):
            item = self.flat_list[self.current]
            self.current += 1
            return item
        # Если мы дошли до конца списка, то вызываем StopIteration
        raise StopIteration

    def _flatten_list(self, lst):
        # Вспомогательный метод для преобразования вложенного списка в одномерный список
        # Принимает вложенный список lst и возвращает одномерный список result
        result = []
        for item in lst:
            # Если элемент является списком, вызываем рекурсивно _flatten_list
            if isinstance(item, list):
                result.extend(self._flatten_list(item))
            else:
                # Если элемент не является списком, добавляем его в результирующий список
                result.append(item)
        return result

def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()