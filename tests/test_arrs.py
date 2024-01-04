from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([1, 2, 3, 4, 5], 5, "test") == "test"
    assert arrs.get([1, 2, 3, 4, 5],3, "test") == 4



def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([1, 2, 3, 4, 5],0, 0) == []
    assert arrs.my_slice([-1, 2, 3, 4, 5],0, 1) == [-1]
    assert arrs.my_slice([1, 2, 3, 4],None, 5) == [1, 2, 3, 4]
