from mlib import format_input, scale_input
import numpy as np
import pytest

@pytest.fixture
def test_array():
    val = np.array(1)
    feature = val.reshape(-1,1)
    return feature

def test_format_input(test_array):
    assert test_array.shape == format_input(2).shape

def test_scale_input(test_array):
    assert int(scale_input(test_array)) == int(np.array([[-9.56513601]]))