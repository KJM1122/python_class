'''
네이버 API 모듈 사용
'''
import final.naver_search_api as naver_blog


def main():
    json_string = naver_blog.naver_blog_search('홍대', 'JSON')
    print(json_string)


main()
