import requests


# 날짜, 시간, 관측소 입력
def request_weather(input_date, input_hour, input_id):
    req_url = 'http://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList?'
    service_key = '서비스 키 필요'
    data_type = 'JSON'
    data_cd = 'ASOS'
    date_cd = 'HR'
    start_dt = input_date
    start_hh = input_hour
    end_dt = input_date
    end_hh = input_hour
    stn_ids = input_id

    url = req_url + 'serviceKey=' + service_key + \
        '&dataType=' + data_type + '&dataCd=' + data_cd + '&dateCd=' + date_cd + \
        '&startDt=' + start_dt + '&startHh=' + start_hh + '&endDt=' + end_dt + '&endHh=' + end_hh + '&stnIds=' + stn_ids

    print(url)

    res_json = requests.get(url).json()
    res = res_json['response']
    body = res['body']
    items = body['items']
    item = items['item']

    return item
