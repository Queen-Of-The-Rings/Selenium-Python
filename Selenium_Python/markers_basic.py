
import pytest

import time



@pytest.mark.slow

def test_slow_operation():

    """This teprist is marked as slow"""
    print("From test_slow_operation")
    time.sleep(2)  # Simulate slow operation

    assert True



@pytest.mark.skip(reason="Feature not implemented yet")

def test_unimplemented_feature():

    """This test will be skipped"""

    assert False



@pytest.mark.skipif(1 == 1, reason="Always skipped conditionally")

def test_always_skipped():

    """This test is conditionally skipped"""

    assert True



@pytest.mark.xfail(reason="Known bug #123")
def test_known_bug():

    """This test is expected to fail"""
    print("From test_known_bug")
    assert False



def test_normal_operation():

    """This is a normal test without markers"""

    assert 2 + 2 == 4