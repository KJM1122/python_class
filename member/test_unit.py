import unittest  # python junit : 파이썬 테스트 자동화 프레임워크


def add(a, b):
    return a + b


'''
1. unittest.TestCase 상속 받는다.
2. 테스트 함수는 이름을 "test_"로 시작해야 한다.
3. 단정문 "assert...()" 결과 비교
4. setUp
'''


class TestAddFunc(unittest.TestCase):
    def setUp(self):
        print('-' * 20)
        print('setUp()')
        print('-' * 20)

    def test_add_positive(self):
        result = add(12, 14)
        print('test_add_positive result:{}'.format(result))
        self.assertEqual(result, 26)

    def test_add_negative(self):
        result = add(-2, -4)
        print('test_add_negative result:{}'.format(result))
        self.assertEqual(result, -6)


# run 테스트
if __name__ == '__main__':
    unittest.main()

# --------------------
# setUp()
# --------------------
# test_add_negative result:-6
# --------------------
# setUp()
# --------------------
# test_add_positive result:26