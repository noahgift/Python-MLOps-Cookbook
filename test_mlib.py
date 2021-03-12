from mlib import format_input
import numpy as np
import pytest

@pytest.fixture
def test_array():
    val = np.array(1)
    feature = val.reshape(-1,1)
    return feature

def test_format_input(test_array):
    assert test_array.shape == format_input(2).shape
