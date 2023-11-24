import pytest


class Compare:
    def __init__(self, nums_list1, nums_list2):
        self.nums_list1 = nums_list1
        self.nums_list2 = nums_list2

    def average_lists(self) -> tuple:
        if not self.nums_list1 or not self.nums_list2:
            raise Exception('Empty list')
        if not isinstance(self.nums_list1, list) \
                or not isinstance(self.nums_list2, list):
            raise TypeError('Not list')
        list_all = [*self.nums_list1, *self.nums_list2]
        if not all(map(lambda i: isinstance(i, int), list_all)):
            raise ValueError('Value Error')
        av_nums_list1 = sum(self.nums_list1) / len(self.nums_list1)
        av_nums_list2 = sum(self.nums_list2) / len(self.nums_list2)
        return av_nums_list1, av_nums_list2

    def compare_lists(self) -> str:
        data = self.average_lists()
        if data[0] > data[1]:
            return 'Первый список имеет большее среднее значение'
        elif data[0] < data[1]:
            return 'Второй список имеет большее среднее значение'
        else:
            return 'Средние значения равны'


class TestCompare:
    def test_result_one(self):
        list_av = Compare([2, 3, 4, 5], [1, 1, 2, 3])
        assert list_av.compare_lists() == 'Первый список имеет большее среднее значение'

    def test_result_two(self):
        list_av = Compare([1, 1, 2, 3], [2, 3, 4, 5])
        assert list_av.compare_lists() == 'Второй список имеет большее среднее значение'

    def test_result_three(self):
        list_av = Compare([1, 1, 1, 1], [1, 1, 1, 1])
        assert list_av.compare_lists() == 'Средние значения равны'

    def test_average_type_one(self):
        list_av = Compare(1, [1, 1, 1, 1])
        with pytest.raises(TypeError):
            list_av.compare_lists()

    def test_average_type_two(self):
        list_av = Compare([1, 1, 1, 1], 1)
        with pytest.raises(TypeError):
            list_av.compare_lists()

    def test_average_type_three(self):
        list_av = Compare([], [])
        with pytest.raises(Exception):
            list_av.compare_lists()

    def test_average_value_one(self):
        list_av = Compare(["1", "1", "1", "1"], [1, 1, 1, 1])
        with pytest.raises(ValueError):
            list_av.compare_lists()

    def test_average_value_two(self):
        list_av = Compare([1, 1, 1, 1], ["1", "1", "1", "1"])
        with pytest.raises(ValueError):
            list_av.compare_lists()


