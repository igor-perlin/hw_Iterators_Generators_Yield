class FlatIterator:
    """
    Итератор, который принимает список списков и возвращает их плоское представление.
    """
    def __init__(self, list_of_list):
        self.data = [elem for sublist in list_of_list for elem in sublist] # Создание одномерного списка элементов из списка списков
        self.index = 0 # Установка индекса на начало списка

    def __iter__(self):
        self.index = 0 # Установка индекса на начало списка при инициализации итератора
        return self

    def __next__(self):
        if self.index < len(self.data): # Если индекс не вышел за пределы списка, то вернуть элемент
            item = self.data[self.index]
            self.index += 1 # Увеличить индекс для получения следующего элемента
            return item
        raise StopIteration  # Если индекс вышел за пределы списка, вызвать исключение StopIteration

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()