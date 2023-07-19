'''
pickle
'''
import pickle


def main():
    profile_file = open("profile.pickle", 'wb')  # 바이너리 형태로 저장

    profile = {"이름": "스누피", "나이": 22, "취미": ["자전거", "골프", "코딩"]}
    print(profile)  # {'이름': '스누피', '나이': 22, '취미': ['자전거', '골프', '코딩']}

    # pickle: 파일에 저장
    pickle.dump(profile, profile_file)  # profile 데이터를 profile_file에 저장
    profile_file.close()

    print('-' * 50)

    profile_file = open('profile.pickle', 'rb')  # 읽어올 때도 바이너리 모드 명시

    profile = pickle.load(profile_file)
    print(profile)  # {'이름': '스누피', '나이': 22, '취미': ['자전거', '골프', '코딩']}
    profile_file.close()


main()
