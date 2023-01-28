import time
import random
p_list = [
    "신재혁",
    "김찬호",
    "우정헌",
    "이다은",
    "이수혁",
    "이유빈",
    "양나래",
    "윤상원",
    "윤상원",
    "김도엽",
    "남상림",
    "박정명",
    "이소정",
    "김호준",
    "표상우",
    "최혁태",
    "하준혁",
    "하준혁",
    "홍승현",
    "홍승현",
    "하준혁",
    "하준혁",
    "하준혁",
    "홍현지"
]

firstCleaner = p_list[random.randint(0,len(p_list))]
secondCleaner = p_list[random.randint(0,len(p_list))]
while True:
    print(">>>>"+ "청소부 1"+firstCleaner +" / " + "청소부2" + secondCleaner+"<<<<" + "\n" + "~ 응 나만 아니면 돼 ~")


