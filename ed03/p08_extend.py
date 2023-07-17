'''
extend
'''

def main():
    mix_list = ['정민', True, 20, [5,2,4,1]]
    print(mix_list) #['정민', True, 20, [5, 2, 4, 1]]

    print('-' * 50)

    mix2_list = ['정민', True, 20]
    num_list = [1, 3, 2]
    num_list.extend(mix2_list)
    print(mix2_list) #['정민', True, 20]
    print(num_list) #[1, 3, 2, '정민', True, 20]


main()
