#만든이 김성건
# 만든 날짜 0324
# 만든 시간 14:01
def gugu(dan) : 
    for i in range(1, 40):
        print(f"{dan} X {i} = {dan * i}")
    
def total_gugu():
        for i in range(1, 40):
            gugu(i)
            print("----------------------")

total_gugu()