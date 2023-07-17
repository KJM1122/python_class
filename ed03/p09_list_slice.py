'''
리스트 슬라이싱
'''

def main():
    num_list = [1,2,3,4,5]
    print(num_list) #[1, 2, 3, 4, 5]

    print(num_list[0:2]) #[1, 2] #0은 포함 2는 미포함

    # 처음부터 1번지까지 출력
    num_01 = num_list[:2]
    print(num_01) #[1, 2]

    # 2번지부터 끝까지
    num_02 = num_list[2:]
    print(num_02)

    print('-' * 50)

    # 중첩 리스트 슬라이싱
    nest_list = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
    print(nest_list) #[1, 2, 3, ['a', 'b', 'c'], 4, 5]

    nest_slice = nest_list[2:5]
    print(nest_slice) #[3, ['a', 'b', 'c'], 4] #리스트 하나가 인덱스 하나

    print(nest_list[3][:2]) #['a', 'b']

    print('-' * 50)

    # 리스트 연산
    num01_list = [1, 2, 3]
    num02_list = [4, 5, 6]

    # 리스트 결합
    print(num01_list + num02_list) #[1, 2, 3, 4, 5, 6]

    # 리스트 곱한 수만큼 반복
    print(num01_list * 3) #[1, 2, 3, 1, 2, 3, 1, 2, 3]

    # 리스트의 길이 구하기
    print(len(num01_list)) #3


main()
