'''
* 찍기
'''

def main():
    index = 1
    while index <= 5:
        print('*' * index)
        index += 1

    print('-' * 50)

    i = 0
    while True:
        i += 1
        print('*' * i)
        if i == 5: break

    # *
    # **
    # ***
    # ****
    # *****

main()
