'''
list 안에 for문, if문
'''

def main():
    data = [1, 2, 3, 4, 5]

    # 짝수에만 3을 곱하기
    result = [num * 3 for num in data if num % 2 == 0]
    print(result) #[6, 12]

main()
