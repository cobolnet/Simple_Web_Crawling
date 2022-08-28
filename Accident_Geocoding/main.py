import pandas
import numpy
from geopy.geocoders import Nominatim


def geocoding(addr):
    geo_location = Nominatim(user_agent="South Korea", timeout=None)
    geo = geo_location.geocode(addr)
    result = {"lat": str(round(geo.latitude, 6)), "lng": str(round(geo.longitude, 6))}

    return result


excelSource = pandas.read_excel("./accident_2015-2020.xlsx", "Sheet1")
arrWeather = excelSource.to_numpy()

count = 0
result_arr = []

for i in range(arrWeather.shape[0]):
    try:
        arr = [arrWeather[i][0], arrWeather[i][1]]
        result = geocoding(arr[1])
        arr.append(result["lat"])
        arr.append(result["lng"])
        print(arr)
        result_arr.append(arr)
    except:
        print("변환불가")
        count = count + 1

print("총 변환 불가 지역 수 ")
print(count)

df = pandas.DataFrame.from_records(result_arr)
df.columns = ['time', 'location', 'lat', 'lng']
df.to_excel('result.xlsx')
