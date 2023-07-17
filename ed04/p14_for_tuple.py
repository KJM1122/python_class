'''
for문에 tuple
'''

def main():
    data = [(1,2), (3,4), (5,6)]

    for (first, last) in data:
        print(first,last)

    # 1 2
    # 3 4
    # 5 6

main()
