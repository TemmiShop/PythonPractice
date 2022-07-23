# Quiz)코딩 대회의 참가율을 높이기 위해 이벤트를 진행한다.
# 댓글 작성자 중 추첨을 통해 1명에게 치킨, 3명에게 커피 쿠폰을 지급한다.
# 1_ 총원 20명이 작성하였고 아이디는 1~20이라고 가정한다.
# 2_ 내용과 상관없이 무작위로 추첨하되 중복은 불가능하다.
# 3_ random모듈의 shuffle과 sample을 활용하라.
print("Quiz 4 :")
import random
id_list=[]

#user=range(1,21) 를 이용해서 생성할 수도 있다
#users=list(users)
for i in range(20): #id 추가하기
    id_list.append(i+1)
random.shuffle(id_list)
winning=random.sample(id_list,4)
winning1st=random.sample(winning,1)
winning.remove(winning1st[0])
print("--당첨자 발표--")
print("치킨 당첨자 : "+str(winning1st))
print("커피 당첨자 : "+str(winning))
print("--축하합니다--")

# Quiz) 50명의 승객과 매칭 기회가 있는 택시 기사가 있다. 총 탑승 승객 수 를 구하라.
# 1_ 운행 소요 시간은 5분~50분 사이의 난수이다.
# 2_ 소요시간 5분~15분 사이의 승객만 매칭하라.
# ex: [0] 1번째 손님 (소요시간 : 15분)
# # ex: 총 탑승 승객 2 분
print("Quiz 4 :")
customerlist=[]
cus_count=0
for i in range(1,51):
    taketime=random.randrange(5,51)
    customerlist.append(taketime)
    if 5<=taketime<=15:
        print(f"[O] {i}번째 손님 탑승합니다. (소요시간 :{taketime}분)")
        cus_count+=1
    else:
        print(f"[X] {i}번째 손님 탑승거부합니다. (소요시간 :{taketime}분)")
print("총 탑승 승객 수 : "+str(cus_count))

# Quiz) 표준 체중을 구하시오
# 1_ 표준 체중은 별도의 함수 내에서 계산
#       함수 : std_weight
#       전달값 : height, gender
# 2_ 소수점 둘째 자리까지 표시
# ex: 키 175cm 남성의 표준 체중 67.38kg 입니다.

def std_weight(height,gender):
    if gender=="여성":
        weight=(height/100)*(height/100)*21
        return weight
    else:
        weight=(height/100)*(height/100)*22
        return weight

height,gender=(172,"남성")
weight=round(std_weight(height,gender),2)
print(f"키{height}cm {gender}의 표준 체중은 {weight} kg입니다.")

height,gender=(164,"여성")
weight=round(std_weight(height,gender),2)
print(f"키{height}cm {gender}의 표준 체중은 {weight} kg입니다.")