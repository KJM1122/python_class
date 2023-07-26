'''

'''


def main():
    s = "aukks"
    skip = "wbqd"
    index = 5

    skip_arr = []
    answer_arr = []

    for i in range(len(skip)):
        skip_arr.append(skip[i])
    print(skip_arr)

    for i in range(len(s)):
        x = ord(s[i])

        for _ in range(index):
            x = x + 1
            for skip in skip_arr:
                if chr(x) == skip:
                    x = x + 1
                if x >= 123:
                    x = x - 26
        answer_arr.append(chr(x))
    answer = ''.join(answer_arr)


main()
