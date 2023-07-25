'''
naver json
'''
import json


def read_json():
    # JSON 문자열
    json_string = '{"name":"Kim", "age":22, "city":"Seoul"}'

    # JSON 문자열 파싱
    parsed_json = json.loads(json_string)

    print('parsed_json: {0}'.format(parsed_json))
    print('parsed_json type: {0}'.format(type(parsed_json)))
    # arsed_json: {'name': 'Kim', 'age': 22, 'city': 'Seoul'}
    # parsed_json type: <class 'dict'> : 파싱 이후 데이터는 딕셔너리

    print('name:{0}'.format(parsed_json['name']))  # name:Kim


def main():
    # read_json()

    data = None

    # JSON 파일 읽기
    with open('naver_blog_20230725.json') as json_file:
        data = json.load(json_file)
    print(type(data), data)  # <class 'dict'>

    # JSON parsing
    jsonArray = data.get('items')  # <class 'dict'>
    for dic_array in jsonArray:
        # print(type(dic_array), dic_array)
        title = dic_array.get('title')
        bloggername = dic_array.get('bloggername')
        postdate = dic_array.get('postdate')
        print('{0} | {1} | {2}'.format(title, bloggername, postdate))

        # 감탄 했던 <b>홍대 맛집</b> 연남동 고기집 우사마 | 김나니의 새콤달콤 라이프 | 20230723
        # 감탄이 절로 나오는 <b>홍대 맛집</b> | Lovelee, Rachelee | 20230517
        # [합정<b>맛집</b>] 가성비 좋은 <b>홍대</b>오마카세 찐<b>맛집</b>:: 카시와 | 美食生活 | 20230712
        # <b>홍대 맛집</b> 추천 군침 싹 도는 파스타 | 뽀네집은 뭘 해 먹나? | 20230719
        # <b>홍대 맛집</b> 토라슌 야끼니꾸 소고기구이 | 김원장의 탐구생활 | 20230717
        # 홍아무도 안하는 <b>홍대 맛집</b> 추천 내가 해본다 | 두근두근.. | 20230404
        # 대박이었던 <b>홍대</b> 점심 <b>맛집</b> | 브로 | 20230718
        # [<b>홍대</b> 수제버거<b>맛집</b>] 제스티살룬 연남 | 성덕은 사랑입니다. | 20230627
        # 한우육회를 무료로 먹을 수 있는 소고기 <b>맛집</b>, 일편등심 <b>홍대</b>본점 | 어썸다움, You are Awesome. | 20230720
        # <b>홍대</b> 소고기 <b>맛집</b> : 아리랑야끼니꾸 | 가성비 좋은 <b>홍대</b> 소고기...  | 에떠의 하루? | 20230615


main()
