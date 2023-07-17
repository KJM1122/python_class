'''
딕셔너리
'''

def main():
    cabinet = {3:'미키', 100:'미니'}

    # key에 해당하는 value
    # 딕셔너리[key]
    print(cabinet[3]) #미키
    print(cabinet[100]) #미니
    print('-' * 30)
    # 딕셔너리.get(key)
    print(cabinet.get(3)) #미키
    print(cabinet.get(100)) #미니

    # 딕셔너리에 없는 key
    print(cabinet.get(99)) #None
    print(cabinet.get(99, '없음')) #없음
    # print(cabinet[99]) 오류

    # key값 유무 확인 : key in 딕셔너리
    print(3 in cabinet) #True
    print(99 in cabinet) #False


main()
