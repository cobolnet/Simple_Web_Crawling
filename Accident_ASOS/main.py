# import sqlalchemy
import pandas
from getJson import request_weather
from mergeExcel import merge_excel

# 결빙 데이터 및 관측소 합치기
mergeArr = merge_excel()
print('==============================')
print(mergeArr)
print('==============================')

# ASOS 관측소로 기상청 데이터 조회하기
# 날짜 형식 yyyymmdd
# 시간 형식 hh

resultArr = []
for i in range(len(mergeArr)):
    print("생성중 " + str(i + 1) + "/" + str(len(mergeArr)))
    date = mergeArr[i][0]
    asosId = mergeArr[i][4]

    newDate = date.strftime("%Y%m%d")
    newHour = date.strftime("%H")

    try:
        weather = request_weather(str(newDate), str(newHour), str(asosId))
        resultArr.append(weather[0])
    except:
        temp = {
                        "tm": "",
                        "rnum": "",
                        "stnId": "",
                        "stnNm": "",
                        "ta": "",
                        "taQcflg": "",
                        "rn": "",
                        "rnQcflg": "",
                        "ws": "",
                        "wsQcflg": "",
                        "wd": "",
                        "wdQcflg": "",
                        "hm": "",
                        "hmQcflg": "",
                        "pv": "",
                        "td": "",
                        "pa": "",
                        "paQcflg": "",
                        "ps": "",
                        "psQcflg": "",
                        "ss": "",
                        "ssQcflg": "",
                        "icsr": "",
                        "dsnw": "",
                        "hr3Fhsc": "",
                        "dc10Tca": "",
                        "dc10LmcsCa": "",
                        "clfmAbbrCd": "",
                        "lcsCh": "",
                        "vs": "",
                        "gndSttCd": "",
                        "dmstMtphNo": "",
                        "ts": "",
                        "tsQcflg": "",
                        "m005Te": "",
                        "m01Te": "",
                        "m02Te": "",
                        "m03Te": ""
                    }
        resultArr.append(temp)
        print("자료 없음")

resultDt = pandas.DataFrame(resultArr)
resultDt.to_excel('asosResults.xlsx')
