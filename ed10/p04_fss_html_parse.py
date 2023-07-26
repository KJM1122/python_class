'''
금융 위원회
금용 용어 사전 파싱
'''
from bs4 import BeautifulSoup
import requests


def parse_fsc_dic(page=1):
    url = 'https://www.fsc.go.kr/in090301?curPage=' + str(page)
    fdic = {}  # 용어:용어설명
    lst_title = []  # 용어명
    lst_content = []  # 용어설명

    try:
        print(f'url: {url}')
        # 금융 위원회 금융 용어 접근
        response = requests.get(url)
        print(f'response: {response.status_code}')  # response: 200
        # print(f'response.content: {response.content}')  # response: <Response [200]>

        if response.status_code == 200:  # 성공적인 요청
            # 객체 생성
            soup = BeautifulSoup(response.content, 'html.parser')

            # 용어명
            titles = soup.select('.subject a')  # subject class 내의 <a>
            for title in titles:
                print('용어명:', title.text)
                lst_title.append(title.text.strip())

            # 설명
            contents = soup.select('div > .info2 p span')  # div 요소의 info2 class 내의 <p> 안의 <span>
            for content in contents:
                print('용어설명:', content.text)
                lst_content.append(content.text.strip())

            # 리스트 -> 딕셔너리 {용어명:용어설명}
            for i in range(len(lst_title)):
                fdic[lst_title[i]] = [lst_content[i]]
            print('fdic: {}'.format(fdic))

        else:
            print('금융 위원회 용어 사전 접근 실패:', url)

    except Exception as e:
        print('오류 발생:', str(e))

    return fdic


def main():
    for page in range(1, 23, 1):
        parse_fsc_dic(page)


main()
