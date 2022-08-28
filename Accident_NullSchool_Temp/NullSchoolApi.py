"""
 널스쿨 정보 조회 api
 문자열로 년,월,일,시각
 배열 형태로 위도 경도

 조회할 hpa 500, 700, 850, 1000 중 하나
 hpa가 0이라면 surface로 설정 됨

 현재 시각 즉시 조회라면 is_current를 True로 설정
 시간 정보는 모두 0으로 설정
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from time import sleep


class NullSchool:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.options.add_argument('lang=ko_KR')
        # self.options.add_argument('window-size=1280,720')
        self.options.add_argument('--disable-extensions')
        self.options.add_argument('disable-gpu')
        self.options.add_argument('disable-infobars')
        self.driver = webdriver.Chrome('chromedriver.exe', options=self.options)
        self.driver.implicitly_wait(3)

        self.time_format = "%Y-%m-%d %H:00"
        self.year = "%Y"
        self.month = "%m"
        self.date = "%d"
        self.hour = "%H"

    # time = "%Y-%m-%d %H:00"
    # location = [latitude, longitude]
    # hpa
    # is_current 일 경우 time 은 None
    def null_school(self,  is_current: bool, time: str, location: tuple, hpa: int):

        """
        ! todo
        버튼 클릭시 데이터가 동적으로 생성 되므로 대기 필요
        sleep 대신 셀레니움에서 제공하는 waits 메소드로 변경 필요
        """
        print("Starting...")

        latitude, longitude = location

        # 주소 요청
        if not is_current:
            var_datetime = datetime.strptime(time, self.time_format)
            year = var_datetime.strftime(self.year)
            month = var_datetime.strftime(self.month)
            date = var_datetime.strftime(self.date)
            hour = var_datetime.strftime(self.hour)

            if hpa == 0:
                self.driver.get(f"https://earth.nullschool.net/" +
                                f"#{year}/{month}/{date}/{hour}00Z/" +
                                f"wind/surface/level/overlay=temp/orthographic=-225.00,0.00,262/" +
                                f"loc={longitude},{latitude}")
            elif hpa == 1000:
                self.driver.get(f"https://earth.nullschool.net/" +
                                f"#{year}/{month}/{date}/{hour}00Z/" +
                                f"wind/isobaric/1000hPa/overlay=temp/orthographic=-225.00,0.00,262/" +
                                f"loc={longitude},{latitude}")
            elif hpa == 850:
                self.driver.get(f"https://earth.nullschool.net/" +
                                f"#{year}/{month}/{date}/{hour}00Z/" +
                                f"wind/isobaric/850hPa/overlay=temp/orthographic=-225.00,0.00,262/" +
                                f"loc={longitude},{latitude}")
            elif hpa == 700:
                self.driver.get(f"https://earth.nullschool.net/" +
                                f"#{year}/{month}/{date}/{hour}00Z/" +
                                f"wind/isobaric/700hPa/overlay=temp/orthographic=-225.00,0.00,262/" +
                                f"loc={longitude},{latitude}")
            elif hpa == 500:
                self.driver.get(f"https://earth.nullschool.net/" +
                                f"#{year}/{month}/{date}/{hour}00Z/" +
                                f"wind/isobaric/500hPa/overlay=temp/orthographic=-225.00,0.00,262/" +
                                f"loc={longitude},{latitude}")

        else:
            if hpa == 0:
                self.driver.get(f"https://earth.nullschool.net/" +
                                f"/#current/" +
                                f"wind/surface/level/overlay=temp/orthographic=-225.00,0.00,262/" +
                                f"loc={longitude},{latitude}")
            elif hpa == 1000:
                self.driver.get(f"https://earth.nullschool.net/" +
                                f"/#current/" +
                                f"wind/isobaric/1000hPa/overlay=temp/orthographic=-225.00,0.00,262/" +
                                f"loc={longitude},{latitude}")
            elif hpa == 850:
                self.driver.get(f"https://earth.nullschool.net/" +
                                f"/#current/" +
                                f"wind/isobaric/850hPa/overlay=temp/orthographic=-225.00,0.00,262/" +
                                f"loc={longitude},{latitude}")
            elif hpa == 700:
                self.driver.get(f"https://earth.nullschool.net/" +
                                f"/#current/" +
                                f"wind/isobaric/700hPa/overlay=temp/orthographic=-225.00,0.00,262/" +
                                f"loc={longitude},{latitude}")
            elif hpa == 500:
                self.driver.get(f"https://earth.nullschool.net/" +
                                f"/#current/" +
                                f"wind/isobaric/500hPa/overlay=temp/orthographic=-225.00,0.00,262/" +
                                f"loc={longitude},{latitude}")
        # sleep(0.5)
        wait = WebDriverWait(driver=self.driver, timeout=60)
        sleep(0.1)
        wait.until_not(EC.text_to_be_present_in_element((By.XPATH, '/html/body/main/div[3]/div[1]/div'), 'Downloading...'))
        wait.until(EC.text_to_be_present_in_element((By.XPATH, '/html/body/main/div[3]/div[1]/div'), ''))
        sleep(0.1)

        # div 태그 내 기온 정보 가져 오기
        panel_value = self.driver.find_element_by_xpath('/html/body/main/div[3]/div[2]/div[3]/div')
        value = str(panel_value.get_attribute('aria-label'))
        value = value.rstrip(" °C")

        print("time (UTC+0): ", time)
        print("hPa: ", hpa)
        print("location: ", location)
        print("temp: ", value)

        return value

    def exit_api(self):
        self.driver.close()
        self.driver.quit()
