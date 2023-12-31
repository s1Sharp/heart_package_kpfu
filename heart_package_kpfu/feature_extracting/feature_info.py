hrv_features_dict = dict(
    HRV_MeanNN="Среднее значение интервалов RR.", HRV_SDNN="Стандартное отклонение интервалов RR.",
    HRV_RMSSD="Квадратный корень из среднего значения квадрата последовательных разностей между соседними интервалами RR. Он эквивалентен (хотя и в другой шкале) SD1, и поэтому излишне сообщать о корреляциях с обоими",
    HRV_SDSD="Стандартное отклонение последовательных разностей между интервалами RR.",
    HRV_CVNN="Стандартное отклонение интервалов RR (SDNN), деленное на среднее значение интервалов RR (MeanNN).",
    HRV_CVSD="Среднеквадратичное значение последовательных разностей (RMSSD), деленное на среднее значение интервалов RR (MeanNN).",
    HRV_MedianNN="Медиана интервалов RR.", HRV_MadNN="Среднее абсолютное отклонение интервалов RR.",
    HRV_MCVNN="Среднее абсолютное отклонение интервалов RR (MadNN), деленное на медиану интервалов RR (MedianNN).",
    HRV_pNN50="Доля интервалов RR, превышающих 50 мс, от общего числа интервалов RR.",
    HRV_pNN20="Доля интервалов RR, превышающих 20 мс, от общего числа интервалов RR.",
    HRV_MinNN="Минимальный из интервалов RR", HRV_MaxNN="Максимальный из интервалов RR",
    HRV_HTI="Треугольный индекс ВСР, измеряющий общее количество интервалов RR, деленное на высоту гистограммы интервалов RR.",
    HRV_TINN="Геометрический параметр ВСР, или, более конкретно, базовая ширина распределения интервалов RR, полученная путем треугольной интерполяции, где ошибка наименьших квадратов определяет треугольник. Это аппроксимация распределения интервала RR.",
    HRV_SD1="Стандартное отклонение перпендикулярно линии идентификации. Это показатель краткосрочных колебаний интервала RR, т.е. вариабельности от удара к удару. Он эквивалентен (хотя и в другом масштабе) RMSSD, и поэтому излишне сообщать о корреляции с обоими.",
    HRV_SD2="Стандартное отклонение вдоль линии идентификации. Индекс долгосрочных изменений ВСР.",
    HRV_SD1SD2="Отношение SD1 к SD2. Описывает соотношение краткосрочных и долгосрочных изменений ВСР.",
    HRV_S="Площадь эллипса, описываемого SD1 и SD2 (pi * SD1 * SD2). Она пропорциональна SD1SD2.",
    HRV_CSI="Сердечный симпатический индекс (Toichi, 1997) - это показатель сердечной симпатической функции, не зависящий от активности блуждающего нерва, рассчитываемый путем деления продольной вариабельности графика Пуанкаре (4*SD2) на его поперечную вариабельность (4*SD1).",
    HRV_CVI="Блуждающий индекс сердца (Toichi, 1997) является показателем парасимпатической функции сердца (активность блуждающего нерва, не подверженная влиянию симпатической активности) и равен логарифму произведения продольной (4*SD2) и поперечной вариабельности (4*SD1).",
    HRV_CSI_Modified="Модифицированный CSI (Jeppesen, 2014), полученный путем деления квадрата продольной изменчивости на ее поперечную изменчивость.",
    HRV_GI="Индекс Гузика, определяемый как расстояние точек над линией тождества (LI) до LI, деленное на расстояние всех точек на графике Пуанкаре до LI, за исключением тех, которые расположены на LI.",
    HRV_SI="Индекс наклона, определяемый как фазовый угол точек над LI, деленный на фазовый угол всех точек на графике Пуанкаре, за исключением тех, которые расположены на LI.",
    HRV_AI="Индекс площади, определяемый как совокупная площадь секторов, соответствующих точкам, расположенным над LI, деленная на совокупную площадь секторов, соответствующих всем точкам на графике Пуанкаре, за исключением тех, которые расположены на LI.",
    HRV_PI="Индекс Порта, определяемый как количество точек ниже LI, деленное на общее количество точек на графике Пуанкаре, за исключением тех, которые расположены на LI.",
    HRV_C1d="вклад замедлений сердечного ритма в кратковременную ВСР",
    HRV_C1a="вклад ускорений сердечного ритма в кратковременную ВСР",
    HRV_SD1d="краткосрочная дисперсия вкладов замедлений (удлинений интервалов RR)",
    HRV_SD1a="краткосрочная дисперсия вкладов ускорений (сокращений интервалов RR)",
    HRV_C2d="вклад замедлений сердечного ритма в долгосрочную ВСР",
    HRV_C2a="вклад ускорений сердечного ритма в долгосрочную ВСР",
    HRV_SD2d="долгосрочная дисперсия вкладов замедлений (удлинений интервалов RR)",
    HRV_SD2a="долгосрочная дисперсия вкладов ускорений (сокращений интервалов RR)",
    HRV_Cd="общий вклад замедлений сердечного ритма в ВСР.",
    HRV_Ca="общий вклад ускорений сердечного ритма в ВСР.",
    HRV_SDNNd="общая дисперсия вкладов замедлений (удлинений интервалов RR)",
    HRV_SDNNa="общая дисперсия вкладов ускорений (сокращений интервалов RR)"
)


def get_hrv_from_file():
    raise NotImplementedError


def get_hrv_features(path=''):
    if path == '':
        return hrv_features_dict.keys()
    else:
        return get_hrv_from_file()


main_hrv_features = hrv_features_dict.keys()


def translate_hrv_feature(feature_name):
    return hrv_features_dict[feature_name]


__all__ = [
    main_hrv_features
]
