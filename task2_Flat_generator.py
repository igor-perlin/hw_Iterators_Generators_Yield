import types


def flat_generator(list_of_lists):
    """
    Генератор, который принимает список списков и возвращает их плоское представление.
    """
    for sublist in list_of_lists:  # Итерация по внешнему списку
        if isinstance(sublist, list):  # Проверка, является ли элемент списка списком
            yield from flat_generator(sublist)  # Рекурсивный вызов функции для элемента-списка
        else:
            yield sublist  # Если элемент не является списком, то его можно вернуть через yield

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()