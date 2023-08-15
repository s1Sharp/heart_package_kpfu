import pytest

from util_logger import get_logger
from heart_package_kpfu.utils.ecg_quality import __find_max_subseq_by_cond

logger = get_logger(__name__)


def test_find_subseq():
    arr2 = [1,3,5,6,7,8]
    res1 = __find_max_subseq_by_cond(arr2, lambda x: x % 2 == 1)
    assert res1 == (0, 3)

    arr2 = [10,30,50,60,62,60,45,50,11,23,45]
    res2 = __find_max_subseq_by_cond(arr2, lambda x: x <= 50)
    assert res2 == (len(arr2)-5, len(arr2))

    arr3 = [1,2,3,4,5,5,5,5,5,4,3,2,1,6,6,6,6,6,6,6,6,6,0]
    res3 = __find_max_subseq_by_cond(arr3, lambda x: x > 5)
    assert res3 == (len(arr3)-1-9, len(arr3) - 1)
