'''
list
'''

def main():
    subway = ['Java', 'Oracle', 'HTML', 'CSS', 'Javascript', 'JSP', 'Spring', 'Python']
    print(subway) #['Java', 'Oracle', 'HTML', 'CSS', 'Javascript', 'JSP', 'Spring', 'Python']

    # 추가 : list 제일 마지막에 추가됨
    subway.append('DJango')
    print(subway) #['Java', 'Oracle', 'HTML', 'CSS', 'Javascript', 'JSP', 'Spring', 'Python', 'DJango']

    # 삽입 : 특정 index에 삽입
    subway.insert(5, 'JQuery')
    print(subway) #['Java', 'Oracle', 'HTML', 'CSS', 'Javascript', 'JQuery', 'JSP', 'Spring', 'Python', 'DJango']

    # 데이터 꺼낸 뒤 기존 리스트에서 제거
    print(subway.pop()) #DJango
    print(subway) #['Java', 'Oracle', 'HTML', 'CSS', 'Javascript', 'JQuery', 'JSP', 'Spring', 'Python']
    print(subway.pop()) #Python
    print(subway) #['Java', 'Oracle', 'HTML', 'CSS', 'Javascript', 'JQuery', 'JSP', 'Spring']

    # 리스트에 있는 모든 데이터를 삭제
    subway.clear()
    print(subway) #[]


main()
