import pytest
from io import BytesIO as StringIO
import sys

from bongotest.depthcheck import get_depths, print_depth


class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


def test_get_depths_no_data_typeerror_raised():
    with pytest.raises(TypeError) as excinfo:
        get_depths()
    assert str(excinfo.value) == 'get_depths() takes at least 1 argument (0 given)'


def test_get_depths_proper_data_expected_depths_tuple_array():
    data = {'a': 1, 'b': 2, 'c': 3, 'd': {'k': 9, 'm': -1}}
    assert get_depths(data) == [('a', 1), ('c', 1), ('b', 1), ('d', 1), ('k', 2), ('m', 2)]


def test_print_depth_with_dict():
    captured_output = StringIO()
    sys.stdout = captured_output
    data = {'key1': 1, 'key2': {'key3': 1, 'key4': {'key5': 4}}}

    print_depth(data)
    sys.stdout = sys.__stdout__

    assert captured_output.getvalue() == 'key1: 1\nkey2: 1\nkey3: 2\nkey4: 2\nkey5: 3\n'


def test_print_depth_with_object():
    person_a = Person('User', '1', None)
    person_b = Person('User', '2', person_a)

    captured_output = StringIO()
    sys.stdout = captured_output
    data = {'key1': 1, 'key2': {'key3': 1, 'key4': {'key5': 4, 'user': person_b}}}

    print_depth(data)
    sys.stdout = sys.__stdout__

    assert captured_output.getvalue() == '{}{}{}'.format(
        'key1: 1\nkey2: 1\nkey3: 2\nkey4: 2\nkey5: 3\n',
        'user: 3\nfather: 4\nfirst_name: 4\nlast_name: 4\n',
        'father: 5\nfirst_name: 5\nlast_name: 5\n'
    )
