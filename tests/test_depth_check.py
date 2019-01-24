import pytest

from bongotest.depthcheck import get_depths


def test_get_depths_no_data_typeerror_raised():
    with pytest.raises(TypeError) as excinfo:
        get_depths()
    assert str(excinfo.value) == 'get_depths() takes at least 1 argument (0 given)'
