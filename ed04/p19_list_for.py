'''
list안에 for문
'''

def main():
    data = [1, 2, 3, 4]
    result = []
    print(data) #[1, 2, 3, 4]
    for num in data:
        result.append(num * 3)
    print(result) #[3, 6, 9, 12]

    print('-' * 50)

    data = [1, 2, 3, 4]
    result = [num * 3 for num in data]
    print(result) #[3, 6, 9, 12]

main()
