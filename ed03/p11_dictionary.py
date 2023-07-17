'''
딕셔너리
'''

def main():
    cabinet = {'A-3':'정민', 'B-100':'흥민'}
    print(cabinet) #{'A-3': '정민', 'B-100': '흥민'}

    # 딕셔너리에 추가
    cabinet['C-3'] = '토트넘'
    print(cabinet) #{'A-3': '정민', 'B-100': '흥민', 'C-3': '토트넘'}

    # 딕셔너리 값 변경
    cabinet['B-100'] = '케인'
    print(cabinet) #{'A-3': '정민', 'B-100': '케인', 'C-3': '토트넘'}

    print('-' * 50)

    # 딕셔너리 key, value 모두 추출
    print(cabinet.keys())   #dict_keys(['A-3', 'B-100', 'C-3'])
    print(cabinet.values()) #dict_values(['정민', '케인', '토트넘'])

    # 딕셔너리 key, value 한꺼번에 추출
    print(cabinet.items()) #dict_items([('A-3', '정민'), ('B-100', '케인'), ('C-3', '토트넘')]) #()는 튜플, 값 변경 불가

    # 딕셔너리 값 전체 삭제
    cabinet.clear()
    print(cabinet) #{}


main()
