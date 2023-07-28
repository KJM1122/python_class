'''

'''


def main():
    s = "aukks"
    skip = "wbqd"
    index = 5
    idx = 0

    for i in range(len(s)):
        for k in range(index+1):
            add_index = ord(s[i])+k
            for j in range(len(skip)):
                #print(chr(add_index), skip[j])
                if chr(add_index) == skip[j]:
                    idx += 1
                if add_index >= 122:
                    add_index = add_index - 26
        print(chr(add_index + idx))
        idx = 0
        print('-' * 20)

main()
