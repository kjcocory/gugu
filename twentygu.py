#만든이 김성건
def gugu(dan) : 
    for i in range(1, 30):
        print(f"{dan} X {i} = {dan * i}")
    
def total_gugu():
        for i in range(1, 30):
            gugu(i)
            print("----------------------")

total_gugu()