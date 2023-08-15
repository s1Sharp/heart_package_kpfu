__info__ = 'https://neuropsychology.github.io/NeuroKit/functions/ecg.html#ecg-quality'

'''
Zhao, Z., & Zhang, Y. (2018). “SQI quality evaluation mechanism of single-lead ECG signal based on simple heuristic fusion and fuzzy comprehensive evaluation”. Frontiers in Physiology, 9, 727.
'''

import neurokit2 as nk
import numpy as np
import pandas as pd

from collections.abc import Iterable, Callable


def __find_max_subseq_by_cond(arr, predicate: Callable):
    lidx, ridx = 0, 0
    result = (lidx, ridx)
    try:
        while lidx < len(arr):
            while ridx < len(arr) and predicate(arr[ridx]):
                ridx += 1
            result = (lidx, ridx) if result[1] - result[0] < ridx - lidx else result
            ridx += 1
            lidx = ridx
    except Exception as e:
        print(f"caught exception as {e}")
    finally:
        return result


def ecg_quality_range(ecg_cleaned: pd.DataFrame, sampling_rate=150, min_quality: int = 50, method: str = 'averageQRS'):
    """
    prepare data before this function like:
        ecg_cleaned = nk.ecg_clean(ecg, sampling_rate=300)

    Returns
    -------
    array or strq
        Vector containing the quality index ranging from 0 to 1 for ``"averageQRS"`` method,
        returns string classification (``Unacceptable``, ``Barely Acceptable`` or ``Excellent``)
        of the signal for ``"zhao2018 method"``.
    """
    ecg_quality_range.methods = ['zhao2018', 'averageQRS']

    if not ecg_cleaned or not isinstance(ecg_cleaned, (pd.DataFrame, pd.Series, tuple, list)):
        raise RuntimeError('ecg_cleaned not valid data')
    if method not in ecg_quality_range.methods:
        raise RuntimeError(f'unknown method, available is {ecg_quality_range.methods}')
    quality = nk.ecg_quality(ecg_cleaned, sampling_rate=sampling_rate, method=method)
    if method == 'zhao2018':
        return str(quality)
    quality_q = np.array(quality).min() + ((np.array(quality).max() - np.array(quality).min()) * min_quality / 100)
    result = __find_max_subseq_by_cond(quality, lambda x: int(x) > int(quality_q))

    return result
