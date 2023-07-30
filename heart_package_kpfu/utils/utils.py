# Load NeuroKit and other useful packages
import neurokit2 as nk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_cardio_data(path = "./Cardio/1.1.csv") -> pd.DataFrame:
    """
    cardio data should have 2 pandas series [ECG, time]
    """
    raw_data = pd.read_csv(path, sep=';')
    for col in raw_data:
        raw_data[col] = raw_data[col].apply(lambda x: str(x).replace(',', '.'))
    
    data = pd.DataFrame()
    data['ECG'] = raw_data['II(длинн.)'].astype(float)
    data['time'] = raw_data['time'].astype(float)

    return data


def calculate_sampling_rate(heart_data: pd.DataFrame) -> float:
    ms_in_one_seconds = 1000
    diff = lambda g: g.max() - g.min()
    timediff = diff(heart_data['time'])
    sampling_rate = (heart_data['ECG'].size - 1) / (timediff / ms_in_one_seconds)
    return sampling_rate


def convert_ecg_data_from_pixel_to_mhz(ecg_data: pd.DataFrame, copy=True):
    pixel_in_one_box = 6
    mhz_in_one_box = 1

    translate_coef = mhz_in_one_box / pixel_in_one_box

    new_data = ecg_data.copy(deep=copy)
    new_data['ECG'] *= translate_coef

    return new_data


def data_min_max_normalization(pd_series: pd.Series):
    return (pd_series-pd_series.min())/(pd_series.max()-pd_series.min())


def prepare_ecg_data(ecg_data: pd.DataFrame, min_max_norm: bool = True, copy: bool = True):
    new_data: pd.DataFrame = ecg_data.copy(deep=copy)
    cols = new_data.select_dtypes(exclude=['float']).columns
    new_data[cols] = new_data[cols].apply(pd.to_numeric, downcast='float', errors='coerce')
    if min_max_norm:
        new_data['ECG'] = data_min_max_normalization(new_data['ECG'])
    # print(f'ecg data min={new_data.min()}:max={new_data.max()}')
    return new_data


def interpolate_heart_data(ecg_data: pd.DataFrame, step: int = 2, method: str = 'index'):
    """
    do not forget multiply sampling_rate to interpolate_step
    """
    new_data = ecg_data.copy(deep=True)
    new_df = pd.DataFrame(index=range(0, len(new_data) * step), columns=new_data.columns, dtype=float)
    for idx in range(0, len(new_data)):
        for col in new_data.columns:
            new_df[col][idx * step] = new_data[col][idx]
    new_df = new_df.interpolate(method=method)
    return new_df

