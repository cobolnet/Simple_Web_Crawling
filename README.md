# Simple_Web_Crawling
셀레니움을 활용한 간단한 웹 크롤링으로 기상청 API와 NullSchool을 활용하여 데이터 수집하기
데이터 수집을 위한 위치 정보는
http://taas.koroad.or.kr/gis/mcm/mcl/initMap.do?menuId=GIS_GMP_STS_RSN#
교통사고 분석 시스템을 조회하였음

Accident_Geocoding = 교통사고 분석 시스템에서 조회한 지역의 대략적 위, 경도 얻기
Accident_ASOS = 기상청 API를 조회하여 사고 지역의 ASOS 측정 정보 얻기
Accident_NullScholl_Rain = 셀레니움을 통해 https://earth.nullschool.net/ 에서 강수량 얻기
Accident_NullSchool_Temp = 셀레니움을 통해 https://earth.nullschool.net/ 에서 기온 정보 얻기
