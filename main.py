from heart_package_kpfu import process_prepared_ecg_data, full_prepare_ecg_data

if __name__=='__main__':
    from heart_package_kpfu import full_prepare_ecg_data, ecg_quality_range

    a = full_prepare_ecg_data('/home/maxim/self/study/heart/Cardio/1.1.csv')
    d, sr = a
    print(type(d["ECG"]))
    print(ecg_quality_range(d["ECG"], sr))
