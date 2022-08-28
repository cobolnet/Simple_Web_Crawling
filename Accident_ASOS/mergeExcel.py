from datetime import datetime
from haversine import haversine
import numpy
import pandas


def merge_excel():
    freezing_data_frame = pandas.read_excel("./accident_2015-2020_results.xlsx", "Sheet1")
    # 결빙 사고 데이터
    freezing_arr = freezing_data_frame.to_numpy()

    point_data_frame = pandas.read_excel("./ASOSPoint.xlsx", "Sheet1")
    # AWS 관측 지점 데이터
    point_arr = point_data_frame.to_numpy()

    date_time_format = "%Y년 %m월 %d일 %H시"

    print(freezing_arr.shape[0])
    print(point_arr.shape[0])

    # 사고 발생 지점 Date 형식 변경하기
    # 사고 발생 지점과 가까운 AWS 관측소 찾기
    append_arr = []
    for i in range(11591, len(freezing_arr)):
        freezing_arr[i][0] = datetime.strptime(freezing_arr[i][0], date_time_format)
        freezing_location = (freezing_arr[i][2], freezing_arr[i][3])
        result = []
        for j in range(point_arr.shape[0]):
            point_location = (point_arr[j][2], point_arr[j][3])
            result.insert(j, haversine(freezing_location, point_location))

        min_value = min(result)
        index = result.index(min_value)
        shortest_aws = point_arr[index]

        append_arr.insert(i, numpy.append(freezing_arr[i], shortest_aws))

    return append_arr
