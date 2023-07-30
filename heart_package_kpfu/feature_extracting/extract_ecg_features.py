# Load NeuroKit and other useful packages
import neurokit2 as nk
import matplotlib.pyplot as plt


from heart_package_kpfu.feature_extracting.feature_info import main_hrv_features
from heart_package_kpfu.types import default_sampling_rate
from heart_package_kpfu.utils.utils import (
    calculate_sampling_rate,
    convert_ecg_data_from_pixel_to_mhz,
    interpolate_heart_data,
    load_cardio_data,
    prepare_ecg_data
)


def process_prepared_ecg_data(ecg_data, sampling_rate = default_sampling_rate, interpolate_step = 1):
    """
    -> load_cardio_data -> calculate_sampling_rate -> convert_ecg_data_from_pixel_to_mhz -> prepare_ecg_data -> interpolate_heart_data
    :return: tuple( figure with heart-rate data, ecg-peak data, feature-info from feature_extracting.main_hrv_features)
    """
    sampling_rate *= interpolate_step

    print(ecg_data)

    signals, info = nk.ecg_process(ecg_data['ECG'], sampling_rate=sampling_rate)

    # Visualise the processing
    nk.ecg_plot(signals, sampling_rate=sampling_rate)
    fig = plt.gcf()

    peaks, peak_info = nk.ecg_peaks(ecg_data['ECG'], sampling_rate=sampling_rate)
    # Compute HRV indices
    hrv_data = nk.hrv(peaks, sampling_rate=sampling_rate, show=False)
    fig_hrv = plt.gcf()

    hrv_data_final = dict()
    for feature in main_hrv_features:
        if feature in hrv_data.keys():
            hrv_data_final[feature] = hrv_data[feature][0]

    return tuple([fig, (signals, info), (peaks, peak_info), fig_hrv, hrv_data_final])



def full_prepare_ecg_data(ecg_file_path: str = "./Cardio/1.1.csv", interpolate_step=2, interpolate_method='index'):
    x = load_cardio_data(ecg_file_path)
    sr = calculate_sampling_rate(x)
    x = convert_ecg_data_from_pixel_to_mhz(x)
    x = prepare_ecg_data(x)
    x = interpolate_heart_data(x, interpolate_step, interpolate_method)
    return process_prepared_ecg_data(x, sr, interpolate_step)