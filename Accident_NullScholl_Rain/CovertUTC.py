"""
 3 시간 단위로 나눴을 때 변환 시간을 기준으로 가장 이른 시간의 데이터를 조회한다.
 (예를 들어 00시 -> 00시, 01시 -> 00시, 02시 -> 00시, 03시 -> 03시 ...)
"""
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pytz


class ConvertUTC:

    def __init__(self):
        self.time_format = "%Y-%m-%d %H:00"
        self.hour_format = "%H"

    def convert_time_to_3hour_utc(self, cur_time: str):
        str_to_datetime = datetime.strptime(cur_time, self.time_format)
        datetime_kst = pytz.timezone('Asia/Seoul').localize(str_to_datetime)

        kst_to_utc = datetime_kst.astimezone(pytz.utc)

        cur_hour = kst_to_utc.strftime(self.hour_format)

        modular = int(cur_hour) % 3

        if modular == 0:
            return kst_to_utc.strftime(self.time_format)
        else:
            kst_to_utc -= relativedelta(hours=modular)
            return kst_to_utc.strftime(self.time_format)
