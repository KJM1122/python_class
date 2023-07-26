'''
XML 파싱
'''
import xml.etree.ElementTree as ET


# Element : XML 문서의 각 요소

def main():
    xml_data = '''
    <bookstore>
        <book>
            <title>점프 투 파이썬</title>
            <author>박응용</author>
            <year>2022</year>
        </book>
        <book>
            <title>파이썬 입문</title>
            <author>나도코딩</author>
            <year>2022</year>
        </book>
    </bookstore>
    '''

    # XML 데이터 파싱
    # ET.parse(filename)  # xml파일에서 읽음
    root = ET.fromstring(xml_data)  # string -> xml

    # Element 클래스를 사용하여 요소의 정보 출력
    print('태그 이름:', root.tag)  # 태그 이름: bookstore
    print('텍스트 내용:', root.text)  # 텍스트 내용:
    print('속성:', root.attrib)  # 속성: {}

    # 하위 요소 정보
    for child in root:
        print('하위 요소 태그 이름:', child.tag)
        print('하위 요소 텍스트 내용:', child.text)
        # 하위 요소 태그 이름: book
        # 하위 요소 텍스트 내용:
        #
        # 하위 요소 태그 이름: book
        # 하위 요소 텍스트 내용:

    # 첫 번째 book element의 하위 element 찾기
    title = root.find("book/title").text
    author = root.find("book/author").text
    year = root.find("book/year").text
    print('첫 번째 책 정보')
    print(f'제목: {title}')
    print(f'저자: {author}')
    print(f'출판연도: {year}')
    # 첫 번째 책 정보
    # 제목: 점프 투 파이썬
    # 저자: 박응용
    # 출판연도: 2022

    print('=' * 50)

    # 모든 book element의 하위 찾기
    books = root.findall("book")
    for book in books:
        title = book.find('title').text
        print(f'제목: {title}')
        author = book.find('author').text
        print(f'저자: {author}')
        year = book.find('year').text
        print(f'출판연도: {year}')
        print('-' * 20)
        # 제목: 점프 투 파이썬
        # 저자: 박응용
        # 출판연도: 2022
        # --------------------
        # 제목: 파이썬 입문
        # 저자: 나도코딩
        # 출판연도: 2022
        # --------------------


main()
