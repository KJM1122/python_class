'''
list
'''

def main():
    subway = ['지수', '제니', '로제', '리사']
    print(subway) #['지수', '제니', '로제', '리사']

    subway.append('지수')
    print(subway) #['지수', '제니', '로제', '리사', '지수']

    print(subway.count('지수')) #2


main()
