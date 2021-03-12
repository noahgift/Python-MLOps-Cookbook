from mlib import format_input, scale_input, height_human
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

def test_height_human():
    assert '6 foot, 1 inches' == height_human(73.4)
    assert '5 foot, 11 inches' == height_human(71.1)