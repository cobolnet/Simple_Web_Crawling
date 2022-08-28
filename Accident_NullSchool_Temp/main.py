from NullSchoolApi import NullSchool
from CovertUTC import ConvertUTC
from datetime import datetime
import pandas
import numpy

nullSchool = NullSchool()
convert_utc = ConvertUTC()

freezing_dataframe = pandas.read_excel("./accident_2015-2020.xlsx", "Sheet1")
freezing_arr = freezing_dataframe.to_numpy()

datetime_kr_format = "%Y년 %m월 %d일 %H시"
datetime_format = "%Y-%m-%d %H:00"

for i in range(0, freezing_arr.shape[0]):
    freezing_arr[i][0] = datetime.strptime(freezing_arr[i][0], datetime_kr_format)
    freezing_arr[i][0] = freezing_arr[i][0].strftime(datetime_format)

append_arr = []
for i in range(0, freezing_arr.shape[0]):
    freezing_time = convert_utc.convert_time_to_3hour_utc(freezing_arr[i][0])
    freezing_loc = (round(freezing_arr[i][2], 3), round(freezing_arr[i][3], 3))

    result = []
    hpa_index = [0, 1000, 850, 700, 500]
    for hpa in hpa_index:
        try:
            value = nullSchool.null_school(is_current=False, time=freezing_time, location=freezing_loc, hpa=hpa)
            result.append(value)
        except:
            result.append("Timeout")

    append_arr.append(result)
    print("status: " + str(i + 1) + "/" + str(freezing_arr.shape[0]))

nullSchool.exit_api()

df = pandas.DataFrame.from_records(append_arr)
df.columns = ['surface', '1000hPa', '850hPa', '700hPa', '500hPa']
df.to_excel('result.xlsx')

