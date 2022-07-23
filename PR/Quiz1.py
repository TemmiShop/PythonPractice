# Quiz)변수를 이용하여 다음 문장을 출력하시오
# 변수명 : station , 변수값 : "사당","신도림","인천공항" 순서대로 입력
# 답 : XX 행 열차가 들어오고 있습니다.

import random
station = ["사당", "신도림", "인천공항"]
next_station = random.choice(station)

print("Quiz 1 :")
print(next_station + "행 열차가 들어오고 있습니다.")

# Quiz)당신은 코딩 스터디 모임을 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인 1번은 오프라인으로 진행합니다
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램 작성하시오
# 1_ 날짜는 랜덤
# 2_ 월별 날짜는 다름을 감안하여 최소 일수인 28일 이내로 정함
# 3_ 매월 1일부터 3일까지 스터디 준비를 위해 제외함

studyday=[]
for i in range(4):
    days=random.randint(4,28) #4일 부터 28일 이하
    while days in studyday:
        days=random.randint(4,28)
    studyday.append(days) #값을 리스트에 추가
print("Quiz 2 :")
print("온라인 스터디 모임 날짜는 매월 "+str(studyday[0])+", "+str(studyday[1])+", "+str(studyday[2])+" 일 입니다")
print("오프라인 스터디 모임 날짜는 매월 "+str(studyday[3])+" 일 입니다")

# Quiz)사이트 별로 비밀번호를 설정하시오
# 1_ http:// 제외
# 2_ 닷컴(.com)  제외
# 3_ 1과 2를 만족하는 첫 세 글자 + 총 글자 개수 + 글자 내 "e"의 개수 + "!"로 구성
# 예) naver의 경우 생성된 비밀번호 : nav51!
print("Quiz 3 :")
print("사용하실 도메인을 입력해주십시오 :")
userinput=input()
userinput=str(userinput)
userdomain=userinput.strip("http://") 
#또는 userinput.replace("http://","")
userdomain=userdomain.strip(".com") 
#또는 userdomain=userdomain[:userdomain.index(".")]
fstpassword=userdomain[0:3]
countlist=len(userdomain)
count_e=userdomain.count("e")
print(f"유저님의 비밀번호는 \"{fstpassword}{countlist}{count_e}!\" 입니다")
#또는
#password=fstpassword+str(len(userdomain))+str(userdomain.count("e"))+"!"
#print("{0}의 비밀번호는 {1}입니다.".format(userinput, password))
