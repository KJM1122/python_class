'''
set
'''

def main():
    java = {"정민", "흥민", "케인", "로메로"}
    python = set(["로메로", "메디슨"])

    print(java) #{'정민', '로메로', '흥민', '케인'} (순서 보장 안 됨)
    print(python, type(python)) #{'메디슨', '로메로'} <class 'set'>

    # 교집합 : &, intersection
    print(java & python) #{'로메로'}
    print(java.intersection(python)) #{'로메로'}

    s2 = set("Hello")
    print(s2) #{'l', 'H', 'o', 'e'} (순서 보장 안 됨, 중복 제거)

    # 합집합 : |, union
    print(java | python) #{'메디슨', '케인', '로메로', '정민', '흥민'}
    print(java.union(python)) #{'메디슨', '케인', '로메로', '정민', '흥민'}

    # 차집합 : -. difference
    print(java - python) #{'정민', '케인', '흥민'}
    print(java.difference(python)) #{'정민', '케인', '흥민'}
    print('-' * 50)

    # 추가: add()
    # 삭제: remove()
    print(python) #{'메디슨', '로메로'}
    python.add('쿨루셉스키')
    print(python) #{'메디슨', '로메로', '쿨루셉스키'}

    print(java) #{'로메로', '흥민', '케인', '정민'}
    java.remove("로메로")
    print(java) #{'흥민', '케인', '정민'}

main()
